#!/usr/bin/env python
# coding: utf-8

# In[1]:


#3
import collections
import numpy as np
class Custom_Alignment:

    
    #3 
    def local_alignment(self, sequence_A: str, sequence_B:str, substitution: dict, gap: int ):
        n = len(sequence_A)
        m = len(sequence_B)
        
        
        # if one of the strings is empty
        if n * m == 0:
            return n + m
        
        # array to store the convertion history
        d = [ [0] * (m + 1) for _ in range(n + 1)]
        
        # init boundaries
        for i in range(n + 1):
            d[i][0] = 0
        for j in range(m + 1):
            d[0][j] = 0
        
        # DP compute 
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = d[i - 1][j] + gap
                down = d[i][j - 1] + gap
                left_down = d[i - 1][j - 1] + substitution[sequence_A[i-1]][sequence_B[j-1]]                    
                d[i][j] = max(left, down, left_down,0)   
        #print(np.matrix(d))
        
        return self.local_traceback(d,sequence_A,sequence_B,gap)

          #3
    def find_max_coordinates(self,score_matrix):
        score=np.array(score_matrix)
        result = np.where(score_matrix == np.amax(score_matrix))
        number_max_coordinates=result[0].size
        max_coords_arr=[]
        for i in range(number_max_coordinates):
          max_coords = (result[0][i], result[1][i])
          max_coords_arr.append(max_coords)
        print(max_coords_arr)
        return max_coords_arr
    
    #3
    def local_traceback(self,score_matrix, seq1, seq2, gap):
        seq1_new, seq2_new = [], []
        res = self.find_max_coordinates(score_matrix)
        print(len(res))
        str_arr=[]
        for k in range(len(res)):
          i=res[k][0]
          j=res[k][1]
          j-=1
          i-=1
          #print(i,j)
          stri_seq1=""
          stri_seq2=""
          stri_seq1+=seq1[i]
          stri_seq2+=seq2[j]
          #print(i,j)
          while score_matrix[i][j] != 0:
              diag = score_matrix[i - 1][j - 1]
              up = score_matrix[i - 1][j]
              left = score_matrix[i][j - 1]
              max_points = max(diag, up, left)
              score_matrix[i][j] = 0
              # diag
              if i > 0 and j > 0 and diag == max_points:
                  stri_seq1+=seq1[i - 1]
                  stri_seq2+=seq2[j - 1]
                  i -= 1
                  j -= 1
              # up
              elif j > 0 and up == max_points:
                  stri_seq1+="_"
                  stri_seq2+=seq2[j - 1]
                  j -= 1
              # left
              else:
                  stri_seq1+="_"
                  stri_seq2+=seq2[i - 1]
                  i -= 1
          str_arr.append((stri_seq1[::-1], stri_seq2[::-1]))
        return str_arr
        
#building the substitution matrix for custom alignment
i=chr
s="divyaboggavarapu"
dictname=collections.Counter(s)
dict1={}
for i in range(97, 123):
    dict2={}
    for j in range(97, 123):
        if (chr(i)==chr(j)):
            val=2
        elif ((chr(i) in dictname) or (chr(j) in dictname)):
            val=1
        else:
            val=-1
        dict2[chr(j)]=val
    dict1[chr(i)]=dict2
ans=Custom_Alignment()
ans=ans.local_alignment("divyaboggavarapu","thequickbrownfoxjumpsoverthelazydog",dict1,-2)
print(ans)


# In[2]:


mat_main=[]
for i in dict1:
    mat=[]
    mat.append(i)
    dict2=dict1[i]
    for j in dict2:
        mat.append(dict2[j])
    mat_main.append(mat)
print(mat_main)
np.matrix(mat_main)


# In[ ]:




