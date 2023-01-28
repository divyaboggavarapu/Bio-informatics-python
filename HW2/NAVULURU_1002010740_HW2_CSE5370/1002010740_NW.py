#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
class Solution:
    #1
        def global_alignment(self, sequence_A: str, sequence_B:str,
         substitution: dict, gap: int ):
            n = len(sequence_A)
            m = len(sequence_B)    

            if n * m == 0:
                return n + m

            d = [ [0] * (m + 1) for _ in range(n + 1)]

            # init boundaries
            for i in range(n + 1):
                d[i][0] = i*gap
            for j in range(m + 1):
                d[0][j] = j*gap

            # DP compute 
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    left = d[i - 1][j] + gap
                    down = d[i][j - 1] + gap
                    left_down = d[i - 1][j - 1] + substitution[sequence_A[i-1]][sequence_B[j-1]]                    
                    d[i][j] = max(left, down, left_down)
            print(d)
            ans=self.global_traceback(d,n,m,sequence_A,sequence_B,gap)
            return ans
        #1
        def global_traceback(self,score_matrix, ls1, ls2, seq1, seq2,gap):
            seq1_new, seq2_new = [], []
            stri_seq1=""
            stri_seq2=""
            i=ls1
            j=ls2
            while i > 0 and j > 0:
                diag = score_matrix[j - 1][i - 1]-1
                up = score_matrix[j - 1][i]+gap
                left = score_matrix[j][i - 1]+gap
                max_points = max(diag, up, left)
                print(max_points)
                # diag
                if diag == max_points:
                    stri_seq1+=seq1[i - 1]
                    stri_seq2+=seq2[j - 1]
                    i -= 1
                    j -= 1
                # up
                elif up == max_points:
                    stri_seq1+=seq1[i - 1]
                    stri_seq2+="_"
                    j -= 1
                # left
                else:
                    stri_seq1+="_"
                    stri_seq2+=seq2[j - 1]
                    j -= 1
            # left border
            while j > 0:
                stri_seq1+="_"
                stri_seq2+=seq2[j - 1]
                j -= 1
            # top border
            while i > 0:
                stri_seq1+=seq1[i - 1]
                stri_seq2+="_"
                i -= 1
            return stri_seq1[::-1], stri_seq2[::-1]
        #1
        def find_max_coordinates(self,score_matrix):
            result = np.where(score_matrix == np.amax(score_matrix))
            max_coords = (result[0][0], result[1][0])
            print(max_coords)
            return max_coords


# In[2]:


d = {'a': {'a':1,'t':-1,'c':-1,'g':-1}, 't':
{'a':-1,'t':1,'c':-1,'g':-1}, 'c':
{'a':-1,'t':-1,'c':1,'g':-1}, 'g':
{'a':-1,'t':-1,'c':-1,'g':1}}
ans=Solution()
ans1 = ans.global_alignment("gata","ctac",d,-2)
print(ans1)


# In[ ]:




