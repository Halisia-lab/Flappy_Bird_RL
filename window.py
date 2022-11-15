import arcade

import tools
import wall


class Window(arcade.Window):
    def __init__(self, agent):
        super().__init__(tools.SCREENWIDTH,
                         tools.SCREENHEIGHT, "Sortie d'urgence")

        self.__agent = agent
        self.__iteration = 0

        self.background = None
        self.sprites = None
        self.walls_sprites = None
        self.ground = None
        self.agent_list = None

    def setup(self):

        self.walls_sprites = arcade.SpriteList()
        self.agent_list = arcade.SpriteList()
        self.background = arcade.load_texture(tools.BACKGROUND)
        self.ground = arcade.load_texture(tools.GROUND)

        self.sprites = dict()
        self.sprites['background'] = self.background
        self.sprites['ground'] = self.ground
        self.sprites['agent'] = self.agent

        first_wall = wall.Wall.create_new_wall(self.sprites, self.height)
        self.walls_sprites.append(first_wall[0])
        self.walls_sprites.append(first_wall[1])

        ####
    #
    #     self.__ground = arcade.SpriteList()
    #     for state in filter(self.__agent.environment.is_ground,
    #                         self.__agent.environment.states):
    #         sprite = arcade.Sprite(':resources:images/tiles/grassCenter.png', tools.SPRITE_SCALE)
    #         sprite.center_x, sprite.center_y = self.state_to_xy(state)
    #         self.__ground.append(sprite)
    #
    #
    #     self.__walls = arcade.SpriteList()
    #     for state in filter(self.__agent.environment.is_wall,
    #                         self.__agent.environment.states):
    #         sprite = arcade.Sprite(':resources:images/tiles/dirtCenter_rounded.png', tools.SPRITE_SCALE)
    #         sprite.center_x, sprite.center_y = self.state_to_xy(state)
    #         self.__walls.append(sprite)
    #
    #
    #     self.__player.center_x, self.__player.center_y \
    #         = self.state_to_xy(self.__agent.state)
    #
    #     self.__goal = arcade.Sprite(':resources:images/items/star.png', tools.SPRITE_SCALE)
    #     self.__goal.center_x, self.__goal.center_y \
    #         = self.state_to_xy(self.__agent.environment.goal)
    #
    #
    # def state_to_xy(self, state):
    #     return (state[1] + 0.5) * tools.SPRITE_SIZE, \
    #            (self.__agent.environment.height - state[0] - 0.5) * tools.SPRITE_SIZE
    def draw_background(self):
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.background.width, self.background.height,
                                      self.background, 0)

    def draw_ground(self):
        arcade.draw_texture_rectangle(self.width // 2, self.ground.height // 2, self.ground.width, self.ground.height,
                                      self.ground, 0)

    def on_draw(self):
        arcade.start_render()
        self.draw_background()
        self.draw_ground()
        self.walls_sprites.draw()
        self.agent_list.draw()

    def on_update(self, delta_time):
        for wall in self.walls_sprites:
            wall.step()
            if wall.right <= 0:
                wall.kill()

            elif len(self.walls_sprites) == 2 and wall.right <= random.randrange(self.width // 2, self.width // 2 + 15):
                new_wall = wall.create_new_wall(self.sprites, self.height)

        wall_crash = arcade.check_for_collision_with_list(self.__agent, self.walls_sprites)

        if new_wall:
            self.walls_sprites.append(new_wall[0])
            self.walls_sprites.append(new_wall[1])

        self.walls_sprites.update()
        #self.agent.update(delta_time)
        self.agent_list.update()

        if wall_crash:
            self.__agent.reset()
            self.__iteration += 1

        if self.__agent.state[1] >= self.walls_sprites[0].center_x and not self.walls_sprites[0].agent_passed:
            self.__agent.score += 1
            self.walls_sprites[0].agent_passed = True
            self.walls_sprites[1].agent_passed = True

            #reward = 300

        if self.__agent.score != self.__agent.environment.goal:
            self.__agent.step()
        else:
            self.__agent.reset()
            self.__iteration += 1
            # self.__sound.play()

        # self.__player.center_x, self.__player.center_y \
        #     = self.__agent.state
