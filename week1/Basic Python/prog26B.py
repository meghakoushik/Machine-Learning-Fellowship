def countOfoccurence(text,char):
  count= 0
  for c in text:
        if c== char:
            count += 1
            return count

text='programming'
charTosearch = 'r'
count= countOfoccurence(text, charTosearch)
print('character count:', count)