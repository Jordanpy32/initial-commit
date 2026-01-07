"""
challenge : List Manipulation

1. Created a list called notes container the values : 12, 9, 15, 8, 14.
2. Display :
   The complete liste
   The first note
   The last note
3. Replaces note 9 by 10
4. Add note 16 at the end of the list
5. Deletes note 8
6. Display final list

"""
# Step 1: Creation of my list
notes = [12, 9, 15, 8, 14]

#Step 2: Display my list
print("My list : notes =",notes)

#Step 3: Display first note
print("First note :",notes[0])

#Step 4: Display last note 
print("Last note :",notes[-1])

#Step 5: Replace note 9 by 10
notes[1] = 10

#Step 6: Add note 16 at the end of the list
notes.append(16)

#Step 7: Deletes note 8
notes.remove(8)

#Step 7: Display final list
print("My final : notes =",notes)