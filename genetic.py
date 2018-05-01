# Homework 4: Solving the Jump-It Game Problem Using a Genetic Algorithm
#
# Authors: Caleb Sutton & Lyubov Sidlinskaya

# Imports
import sys
import random
import jump_it_DP
import time

# Main function executing the genetic algorithm for each puzzle
# should return the most fit chromosome after a specified number
# of generations
def artificial_selection(population, puzzle, max_generations, min_generations, pop_size):
	generation_num = 1
	fitness_streak = 0
	current_most_fit = population[0]
	previous_most_fit = population[0]
	while generation_num <= max_generations and (generation_num <= min_generations or (fitness_streak/generation_num) < 0.5):
		previous_most_fit = current_most_fit
		new_generation = []
		for _ in range(pop_size//2): # double population
			parent1, parent2 = select_parents(population)
			new_generation.append(crossover(parent1, parent2, puzzle))
			new_generation.append(crossover(parent2, parent1, puzzle))
		population = population + new_generation
		while len(population) != pop_size:
			reduce_pop(population)


		for chromosome in population:
			if chromosome['fitness'] < current_most_fit['fitness']:
				current_most_fit = chromosome

		if current_most_fit['fitness'] == previous_most_fit['fitness']:
			fitness_streak += 1

		generation_num += 1

	#print('Total Generations: ' + str(generation_num - 1))

	return current_most_fit


# Function which chooses a chromosome using the roulette wheel
# selection mechanism and removes it from the population
def reduce_pop(population):
	total_cost = 0
	selection_pool = []

	random.seed()

	for chrom in population:
		total_cost += chrom['fitness']

	previous_chance = 0
	for chrom in population:
		chance = chrom['fitness'] / total_cost
		selection_pool.append({'chance': chance, 'chromosome': chrom, 'window': [previous_chance, previous_chance + chance]})

		previous_chance += chance

	selector = random.uniform(0, 1)

	for chrom in selection_pool:
		if selector >= chrom['window'][0] and selector < chrom['window'][1]:
			population.remove(chrom['chromosome'])
			break

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
		selection_pool.append({'chance': chance, 'chromosome': chrom,'window': [previous_chance, previous_chance + chance]})
		previous_chance += chance

	selector1 = random.uniform(0, 1)    # generate a random number that will choose a parent
	selector2 = random.uniform(0, 1)


	for chrom in selection_pool:
		if selector1 > chrom['window'][0] and selector1 < chrom['window'][1]:
			while selector2 >= chrom['window'][0] and selector2 < chrom['window'][1]:    # as long as the second selector fall with in the selection of range of the first parent generate a new random selector
																						# the point of this is so both of the parents arent the same chromosome
				selector2 = random.uniform(0, 1)
			parent1 = chrom['chromosome']
			selection_pool.remove(chrom)

	for chrom in selection_pool:
		if selector2 >= chrom['window'][0] and selector2 < chrom['window'][1]:
			parent2 = chrom['chromosome']
			selection_pool.remove(chrom)

	return(parent1, parent2)


# Function which creates an offspring using the alleles of 
# parent1 and parent2, also determines the fitness of the 
# offspring and returns the representative dictionary
# {alleles: [], fitness: (total cost)}
#
# Note: need to be careful about bug which could produce
#    a chromosome with consecutive 0s
def crossover(parent1, parent2, puzzle):
	cross_point = random.randint(0, len(parent1['alleles']) - 2)
	offspring = {'alleles': [], 'fitness': 0}

	while (parent1['alleles'][cross_point] == 0 and parent2['alleles'][cross_point + 1] == 0): # generate a new cross point as long as 
		cross_point = random.randint(0, len(parent1['alleles']) - 2)

	for i in range(len(parent1['alleles'])):
		if i < cross_point + 1:
			offspring['alleles'].append(parent1['alleles'][i])
		else:
			offspring['alleles'].append(parent2['alleles'][i])

	offspring['fitness'] = get_fitness(offspring['alleles'], puzzle)

	return offspring


# Function which randomly decides whether or not to alter
# one of the chromosomes alleles. Should only happen rarely
def mutate(chromosome):
	random.seed()
	match = 1
	return_val = False

	if random.randint(1, 100) == match: # 1% chance of a mututation
		i = random.randint(0, len(chromosome['alleles']) -2)
		if chromosome['alleles'][i] == 0:   # if the allele is a 0 we can just flip it to a 1 now worries
			chromosome['alleles'][i] = 1
			return_val = True
		else: # if it's a 1 we need to make sure the adjacent alleles are also 1 in order to flip to zero
			if i == 0 and i + 1 < len(chromosome['alleles']):   # Case: first allele
				if  chromosome['alleles'][i + 1] == 1:          # Only Check the next allele
					chromosome['alleles'][i] = 0
					return_val = True
			elif i == len(chromosome['alleles']) - 1:           # Case: last allele cannot be 0
				chromosome['alleles'][i] = 1					# should never get here....
				return_val = False
			elif chromosome['alleles'][i + 1] == 1 and chromosome['alleles'][i - 1] == 1:   # Case: Somewhere in middle, check previous and next allele
				chromosome['alleles'][i] = 0
				return_val = True

	return return_val


# function which returns the the fitness of an array of
# of alleles using the ***fitness function***
def get_fitness(alleles, puzzle):
	board = puzzle[1:]
	fittness_count = 0

	for i in range(len(board)):
		if alleles[i] == 1:
			fittness_count += board[i]

	return fittness_count


# function whcih generates a population of chromosomes
# of size pop_size and populates the alleles of each
# chromosome
def create_random_population(puzzle, pop_size):
	population = []
	pop_item_length = len(puzzle) -2

	random.seed()

	for length in range(pop_size):
		chrom = {'alleles' : [], 'fitness': 0}
		for i in range(pop_item_length):
			bit = random.randint(0, 1)
			if i > 0 and bit == 0:
				if chrom['alleles'][i-1] == 0:
					chrom['alleles'].append(1)
				else:
					chrom['alleles'].append(bit)
			else:
				chrom['alleles'].append(bit)

		chrom['alleles'].append(1) # The last place in the bitstring is always visited

		chrom['fitness'] = get_fitness(chrom['alleles'], puzzle)
		population.append(chrom)

	return population


def print_path(puzzle, alleles):
	i = 1
	print('path showing indices of visited cells: 0', end = "")
	path_contents = '0'
	for bit in alleles:
		if bit == 1:
			print(' -> ' + str(i), end = "")
			path_contents += ' -> ' + str(puzzle[i])
		i += 1
	
	print('\npath showing contents of visited cells: ' + path_contents)
	
	return True

# function which reads the input file and returns an array
# of all the puzzles
def read_data(input_file):
	list_table = []
	try:
		with open(input_file, "r") as data_file:
			for line in data_file:
				item = line.split() #  removes EOL marker
				item = list(map(int, item))
				list_table.append(item)

		return list_table

	# Throw error if issue reading file.
	except IOError:
		print("Error reading file.", input_file)
		sys.exit()

# function which calls artificial_selection() and dynamic_programming()
# for each puzzle and prints the results to the console
def main():
	num_correct = 0
	num_total = 0
	max_pop = 128
	max_generations = 100
	min_generations = 25
	initial_pop = 512
	# for each puzzle call artificial_selection() and dynamic_programming()
	#    and print the results
	if len(sys.argv) > 1:
		initial_time = time.time()

		input_file_name = sys.argv[1]                    # Accepts filename as cmd line argument
		input_table = read_data(input_file_name)
		for puzzle in input_table:
			print('\n\nGame Board: ' + str(puzzle))

			print('________________________________________\nDP Solution')
			cost = [0] * len(puzzle) #create the cache table
			path = cost[:] # create a table for path that is identical to path
			min_cost = jump_it_DP.jumpIt(puzzle, cost, path)
			print("cost: " + str(min_cost))
			jump_it_DP.displayPath(puzzle, path)

			print('________________________________________\nGA Solution')
			pop_size = 2 ** (len(puzzle) - 2)
			if pop_size > max_pop:
				pop_size = max_pop
			most_fit = artificial_selection(create_random_population(puzzle, initial_pop), puzzle, max_generations, min_generations, pop_size)
			print('Cost: ' + str(most_fit['fitness']))
			print_path(puzzle, most_fit['alleles'])

			print('========================================')

			if int(min_cost) == int(most_fit['fitness']):
				num_correct += 1

			num_total += 1

		final_time = time.time()

		print('\n\n\nGA accuracy: ' + str((num_correct/num_total) * 100) + '%')
		print('Total time elapsed: ' + str(final_time - initial_time))

	else:
		print ("Please enter the correct cmd line arguments in the format:")
		print ("python genetic.py input1.txt")


main()
