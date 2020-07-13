#Finding longest substring with no repetitive characters
#code to be fixed..

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = []
        count = 0
        for i in s[0:len(s)-1]:
            for j in s[s.index(i)+1:len(s)-1]:
                if s.index(i)!=s.index(j) and i!=j:
                    count += 1
                    l.append({i:j})
                else:
                    print({i:count},end= " ")
                    count = 0
                break
            return count
 
Solution.lengthOfLongestSubstring(self="test",s="welcomeworld")












        

    

            



        

        
            



            

        


    
            

            