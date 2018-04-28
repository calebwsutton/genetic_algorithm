# Homework 4: Solving the Jump-It Game Problem Using a Genetic Algorithm
#
# Authors: Caleb Sutton & Lyubov Sidlinskaya

# Imports
import sys

###############################################################################
# This is just a quick skeleton I typed up, we will probably have to make some
# structural changes to it, but I think it basically plans out everything we
# need to implement. 
# 
# We still need to decide on a selection mechanism for choosing parents, a
# selection mechanism for choosing which chromosomes to kill, and a fitness
# function
###############################################################################



# Main function executing the genetic algorithm for each puzzle
# should return the most fit chromosome after a specified number
# of generations
#
# Function outline:
#    For each generation
#         select parents and generate offspring
#         population = population + offspring
#         select survivors from population(keep population a consistant size)
#         population = survivors        
#
def artificial_selection(population, puzzle, num_generations, pop_size):

    #  for i in range(num_generations):
    #       for i in range(population_size/2):
    #            population.append(crossover(select_parents(population))) # this will probably throw an error, can you pass arguments as a tuple??
    #       while(len(population) != pop_size) # this is definetly throwing an error
    #            kill_unfit(population)

     # determine most fit chomosome

    return most_fit



# Function which chooses a chromosome using the ***selection mechanism***
# and removes it from the population
def kill_unfit(population):
     # ToDo

     return true




# Function whcih chooses two parents from a population
# based on ***selection mechanism***
#
# Note: for bonus we can implement multiple selection methods
def select_parents(population):
     # ToDo

     return(parent1, parent2)



# Function which creates an offspring using the alleles of 
# parent1 and parent2, also determines the fitness of the 
# offspring and returns the representative dictionary
# {alleles: [], fitness: (total cost)}
#
# Note: need to be careful about bug which could produce
#    a chromosome with consecutive 0s
def crossover(parent1, parent2):
     # ToDo
     
     return offspring



# Function which randomly decides whether or not to alter
# one of the chromosomes alleles. Should only happen rarely
def mutate(chromosome):
     # ToDo

     return false



# function which returns the the fitness of an array of
# of alleles using the ***fitness function***
def get_fitness(alleles, puzzle):
     # ToDo
     # Probably a one liner

     return fitness



# function whcih generates a population of chromosomes
# of size pop_size and populates the alleles of each
# chromosome
def create_random_population(puzzle, pop_size):
     # ToDo
     population = []

     # create list of chromosomes
     # {alleles: [], fitness: int(total cost)}

     return population



# function which reads the input file and returns an array
# of all the puzzles
def read_data(input_file):
    list_table =[]
    try:
        with open(input_file, "r") as data_file:
            for line in data_file:
                item = line.split() #  removes EOL marker
                item = list(map(int, item))
                list_table.append(item)

        return (list_table)

    # Throw error if issue reading file.
    except IOError:
        print ("Error reading file.", input_file_name)
        sys.exit()

# function which calls artificial_selection() and dynamic_programming()
# for each puzzle and prints the results to the console
def main():
 
     # for each puzzle call artificial_selection() and dynamic_programming()
     #    and print the results
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]                    # Accepts filename as cmd line argument
        input_table = read_data(input_file_name) 
        for line in input_table:
            # Send to function
            print (line)
            #genetic_algorithm(line)    
    else:
        print ("Please enter the correct cmd line arguments in the format:")
        print ("python genetic.py input1.txt")


main()
