import numpy as np
# Importing numpy tools for matrix


class wall:
    # Building a cell with wall and empty spaces through matrix
    def __init__(self,row,column):
        # Defining Map
        self.mdp_matrix = np.zeros((row,column))
        self.column = column
        self.row = row

        for i in range(column):
            self.mdp_matrix[0][i] = 1
            self.mdp_matrix[row-1][i] = 1

        for j in range(row):
            self.mdp_matrix[j][0] = 1
            self.mdp_matrix[j][column-1] = 1

        self.mdp_matrix[2][2] = 1
        self.mdp_matrix[1][column-2] = 0
        self.mdp_matrix[2][column-2] = 0

        print(self.mdp_matrix)


        # For rewards
        self.reward = np.zeros((row,column))
        for i in range(row):
            for j in range(column):
                self.reward[i][j] = 0.04

        self.reward[1][column-2] = 1
        self.reward[2][column-2] = -1
        print(self.reward)

        # For initialising U values
        self.U = np.zeros((row,column))
        print(self.U)

    def mdp(self):
        running = True
        iter = 0
        Y = 0.99
        e = 0.01
        while running:
            exceed_threshold = 0
            U_previous = np.zeros((self.row, self.column)) + self.U
            for i in range(self.row):
                for j in range(self.column):
                    if not self.mdp_matrix[i][j]:
                        # Up condition
                        uup = 0
                        if self.mdp_matrix[i-1][j]:
                            uup+=0.8*U_previous[i][j]
                        else:
                            uup+=0.8*U_previous[i-1][j]
                        if self.mdp_matrix[i][j+1]:
                            uup+=0.1*U_previous[i][j]
                        else:
                            uup+=0.1*U_previous[i][j+1]
                        if self.mdp_matrix[i][j-1]:
                            uup+=0.1*U_previous[i][j]
                        else:
                            uup+=0.1*U_previous[i][j-1]

                        udn = 0
                        if self.mdp_matrix[i+1][j]:
                            udn+=0.8*U_previous[i][j]
                        else:
                            udn+=0.8*U_previous[i+1][j]
                        if self.mdp_matrix[i][j+1]:
                            udn+=0.1*U_previous[i][j]
                        else:
                            udn+=0.1*U_previous[i][j+1]
                        if self.mdp_matrix[i][j-1]:
                            udn+=0.1*U_previous[i][j]
                        else:
                            udn+=0.1*U_previous[i][j-1]

                        ur = 0

                        if self.mdp_matrix[i][j+1]:
                            ur+=0.8*U_previous[i][j]
                        else:
                            ur+=0.8*U_previous[i][j+1]
                        if self.mdp_matrix[i+1][j]:
                            ur+=0.1*U_previous[i][j]
                        else:
                            ur+=0.1*U_previous[i+1][j]
                        if self.mdp_matrix[i-1][j]:
                            ur+=0.1*U_previous[i][j]
                        else:
                            ur+=0.1*U_previous[i-1][j]

                        ul = 0
                        if self.mdp_matrix[i][j-1]:
                            ul+=0.8*U_previous[i][j]
                        else:
                            ul+=0.8*U_previous[i][j-1]
                        if self.mdp_matrix[i+1][j]:
                            ul+=0.1*U_previous[i][j]
                        else:
                            ul+=0.1*U_previous[i+1][j]
                        if self.mdp_matrix[i-1][j]:
                            ul+=0.1*U_previous[i][j]
                        else:
                            ul+=0.1*U_previous[i-1][j]

                        if self.reward[i][j] == 1:
                            self.U[i][j] = self.reward[i][j]
                        elif self.reward[i][j] == -1:
                            self.U[i][j] = self.reward[i][j]
                        else:
                            self.U[i][j] = self.reward[i][j] + Y * max(uup,udn,ur,ul)

                        # check convergence
                        diff_U = np.abs(self.U[i][j] - U_previous[i][j])
                        if diff_U > e*(1-Y)/Y:
                            # continue
                            exceed_threshold += 1

            if exceed_threshold == 0:
                running = False

            # Display result
            iter += 1
            print ("Number of Iterations: ",iter)
            print ("Computed Utilities:",self.U)




mdp_matrix = wall(5,6)
mdp_matrix.mdp()
