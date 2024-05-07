import Assignment_Problem_Ph2 
import numpy as np

class Test:
    hun=Assignment_Problem.HungarianAlgorithm()
    
import time

class Test:
    hun = Assignment_Problem.HungarianAlgorithm()
    
    def evaluate(self, cost_matrix):
        '''
        Evaluate the performance of the Hungarian algorithm on a given cost matrix.
        '''
        # Record start time
        start_time = time.time()
        
        # Get the element position using Hungarian algorithm
        ans_pos = self.hun.hungarian_algorithm(cost_matrix.copy())
        
        # Calculate the matrix cost
        ans = self.hun.cost_calculation(cost_matrix, ans_pos)
        
        
        # Generate the binary assignment problem result matrix
        ans_mat_binary = self.hun.binary_matrix(cost_matrix, ans_pos)

        # Record end time
        end_time = time.time()
        
        # Calculate computational time
        computational_time = end_time - start_time
        
        # Show the result including computational time
        print(f"Binary Assignment problem result:\n{ans_mat_binary}")
        print(f"Assignment problem cost result: {ans:.0f}")
        print(f"Computational time: {computational_time} seconds")
            

            
    def testcase1(self):
            array_5x5 = np.random.randint(0, 100, size=(5, 5))
            print("------------------------Test case 1------------------------")
            print("Cost matrix of size 5x5")
            print(array_5x5)
            self.evaluate(array_5x5)
                   
    def testcase2(self):
            array_10x10 = np.random.randint(0, 100, size=(10, 10))
            print("------------------------Test case 2------------------------")
            print("Cost matrix of size 10x10")
            print(array_10x10)
            self.evaluate(array_10x10)
            
    def testcase3(self):
            array_12x12 = np.random.randint(0, 500, size=(12, 12))
            print("------------------------Test case 3------------------------")
            print("Cost matrix of size  12x12")
            print(array_12x12)
            self.evaluate(array_12x12)  
                     
    def testcase4(self):
            array_14x14 = np.random.randint(0, 200, size=(14, 14))
            print("------------------------Test case 4------------------------")
            print("Cost matrix of size  14x14")
            print(array_14x14)
            self.evaluate(array_14x14)     
            
    def testcase5(self):
            array_18x18 = np.random.randint(0, 400, size=(18, 18))
            print("------------------------Test case 5------------------------")
            print("Cost matrix of size 18x18")
            print(array_18x18)
            self.evaluate(array_18x18) 
                
    def testcase6(self):
            array_20x20 = np.random.randint(0, 100, size=(20, 20))
            print("------------------------Test case 6------------------------")
            print("Cost matrix of size 20x20")
            print(array_20x20)
            self.evaluate(array_20x20)  
            
    def testcase7(self):
            array_24x24 = np.random.randint(0, 300, size=(24, 24))
            print("------------------------Test case 7------------------------")
            print("Cost matrix of size 24x24")
            print(array_24x24)
            self.evaluate(array_24x24)     
            
    def testcase8(self):
            array_30x30 = np.random.randint(0, 200, size=(30, 30))
            print("------------------------Test case 8------------------------")
            print("Cost matrix of size 30x30")
            print(array_30x30)
            self.evaluate(array_30x30)         
            
            
            
    def main(self):
     '''
     Perform the testing by calling the test cases
     '''
     np.random.seed(42)
     self.testcase1()
     self.testcase2()
     self.testcase3()
     self.testcase4()  
     self.testcase5()  
     self.testcase6()
     self.testcase7()
     self.testcase8()
       
if __name__ == '__main__':
 Test().main()