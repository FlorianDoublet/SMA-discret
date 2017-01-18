from model.wator.reproductible_creature import ReproductibleCreature


class Fish(ReproductibleCreature):
    def __init__(self, breed_time, color, x, y, env, is_trace):
        super().__init__(breed_time, color, x, y, env, is_trace)
        self.print_cvs_change("born")

    def update(self):
        self.reset_old_position_in_env()
        self.reproduce(self.previous_x, self.previous_y) # Se reproduit juste avant de bouger
        self.environnement.set_agent(self)

    def reproduce(self, x, y):
        if self.maturity > self.breed_time:
            baby = Fish(self.breed_time, "green", x, y, self.environnement, self.is_trace)
            self.environnement.SMA.agent_list.append(baby)
            self.environnement.set_agent(baby)
            self.maturity = 0
        else:
            self.maturity += 1
        pass

    def decide(self):
        if self.age > self.breed_time:
            self.color = "blue"

        self.age += 1
        x, y = self.next_position()

        collision = self.environnement.is_their_a_collision(x, y)

        if collision:
            pass # Collision => no movements
        else:
            self.save_previous_pos()
            self.x = x
            self.y = y
            self.update()

    def next_position(self):
        """
        donne la prochaine position selon la direction de la particule
        :return: x, y qui correspondent a la position
        """

        x, y = self.direction.random_dir()
        x += self.x
        y += self.y

        x, y = self.calculate_torrique_position(x, y)

        return x, y

    def wall_collision(self, wall_inv):
        pass

    def print_cvs_change(self, cause):
        if self.is_trace:
            print("Fish;at;x;" + str(
                self.x) + ";y;" + str(self.y) + ";cause;" + cause)
