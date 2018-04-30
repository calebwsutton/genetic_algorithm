# Homework 4: Solving the Jump-It Game Problem Using a Genetic Algorithm
#
# Authors: Caleb Sutton & Lyubov Sidlinskaya

# Imports
import sys
import random
# import jump_it_DP



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
     total_cost = 0

     return True



# Function whcih chooses two parents from a population
# based on roulette wheel selection mechanism
#
# Note: for bonus we can implement multiple selection methods
def select_parents(population):
    total_fitness = 0
    selection_pool = []

    random.seed()

    for chrom in population:
        total_fitness += 1 / chrom['fitness'] # find the total fitness of the population

    previous_chance = 0
    for chrom in population:
        chance = (1/chrom['fitness']) / total_fitness # this is the percentage chance each chromosome will be selected
        selection_pool.append({'chance': chance, 'chromosome': chrom,'window': [previous_chance, previous_chance + chance]})    # each chromosome is given a window to get selected that lies somewhere in the range of 0 - 1. 
                                                                                                                                # The windows should not overlap and each should be proportional to the chance of getting
                                                                                                                                # selected, so that when a random float is generated bewteen 0 - 1 it will fall into the window of
                                                                                                                                # one of the chromosomes in the selection pool.

                                                                                                                                # ie one might be 0.0 - 0.2, the next might be 0.2 - 0.21, then 0.21-0.7, etc......
                                                                                                                                
        previoius_chance += chance


    selector1 = random.uniform(0, 1)    # generate a random number that will choose a parent
    selector2 = random.uniform(0, 1) 

    # 
    for chrom in selection_pool:
        if selector1 > chrom['window'][0] and selector1 < chrom['window'][1]:
            while selector2 > chrom['window'][0] and selector2 < chrom['window'][1]:    # as long as the second selector fall with in the selection of range of the first parent generate a new random selector
                                                                                        # the point of this is so both of the parents arent the same chromosome
                selector2 = random.uniform(0,1)
            parent1 = selection_pool.pop(chrom)

    for chrom in selection_pool:
        if selector2 > chrom['window'][0] and selector2 < chrom['window'][1]:
            parent2 = selection_pool.pop(chrom)


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

     return False


# function which returns the the fitness of an array of
# of alleles using the ***fitness function***
def get_fitness(alleles, puzzle):
    board = puzzle[1:]
    fittness_count = 0

    for i in range(len(alleles)):
        if alleles[i] == 1:
            fittness_count += board[i]
            
    return fittness_count


# function whcih generates a population of chromosomes
# of size pop_size and populates the alleles of each
# chromosome
def create_random_population(puzzle):
    population = []
    pop_item_length = len(puzzle) -2
    pop_size = 50

    random.seed()

    for length in range(pop_size):
        chrom = {'alleles' : [], 'fitness': 0}
        for i in range(pop_item_length):
            bit = random.randint(0,1)
            if (i > 0 and bit == 0):
                if chrom[i-1] == 0:
                    chrom['alleles'].append(1)
                else:
                    chrom['alleles'].append(bit)
            else:
                chrom['alleles'].append(bit)

        chrom['alleles'].append(1) # The last place in the bitstring is always visited

        # if chrom in population:
        #     continue
        # else:

        chrom['fitness'] = get_fitness(chrom['alleles'], puzzle)
        population.append(chrom)

    # print ("\nChromosome:     Fitness:")

    # for item in population:
    #     item.append(1)      # The last place in the bitstring is always visited
    #     fitness = get_fitness(item, puzzle)

    #     #Not actually saving the fitness value, just printing.
    #     print (item, fitness)
        
    # create list of chromosomes
    # {alleles: [], fitness: int(total cost)}
    # print (population)

    return population

def print_data():

    # global cost, path
    #     cost = [0] * len(lyst) #create the cache table
    #     path = cost[:] # create a table for path that is identical to path
    #     min_cost = jump_it_DP.jumpIt(lyst)
    #     print("game board:", lyst)
    #     print("cost: ", min_cost)
    #     displayPath(lyst)
    #     print("___________________________")
    return True

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
            pop = create_random_population(line)

    else:
        print ("Please enter the correct cmd line arguments in the format:")
        print ("python genetic.py input1.txt")


main()
