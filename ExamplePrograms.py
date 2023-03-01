# Write a function that accepts a list of ints as input and returns each value to the power of 2
def power(stocks):
    output = [x**2 for x in stocks]
    return output

# Write a function to get the avg of grades in a class
def aveGrades(grades):
    return sum(grades) // len(grades)

# Write a Function to reverse a string
def reverseString(string):
    return string[::-1]

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
def twoSum(nums, target):
    hashmap = {}
    for i, j in enumerate(nums):
        if target - j in hashmap:
            return [i, hashmap[target - j]]
        else:
            hashmap[j] = i


#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
def maxProfit(prices):
    profit = 0
    l = 0
    for r in range(1, len(prices)):

        if prices[r] < prices[l]:
            l = r
        profit = max(profit, abs(prices[r] - prices[l]))

    return profit

# Write a function which takes in list of numbers and return True if the list containes dulicates
def containsDulicates(nums):
    return len(nums) != len(set(nums))


