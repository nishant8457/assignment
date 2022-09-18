import sys
from solution import Solution

if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
        if days == 0:
            raise Exception ("Days should be atleast greater than or equal to 1")
        print(f"Total number of days as input {days}")
    except IndexError:
        print("Please pass 'days' argument in command line")
    except ValueError:
        print("'Days' argument must be of integer type")
    except Exception as e:
        print(e)
    else:
        solution = Solution(days)
        solution_1 = solution._valid_number_of_days()
        solution_2 = solution._remove_common()
        print(f'final solution {str(solution_2)}/{str(solution_1)}')