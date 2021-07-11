import io

inputfile = "C:\\Users\\bao\\OneDrive\\Desktop\\test\\input.txt"
existIDfile = "C:\\Users\\bao\\OneDrive\\Desktop\\test\\exist.txt"
outputfile = "C:\\Users\\bao\\OneDrive\\Desktop\\test\\output.txt"
groupId = "557295677987925"
user_id_stop = "100070411418614"

fi = io.open(inputfile, mode="r", encoding="utf-8")
fi1 = io.open(existIDfile, mode="r", encoding="utf-8")
fo = io.open(outputfile, "w")
str = fi.read()
existIDs = fi1.read().splitlines()
#print(existIDs)



def getNumber(str, start_str):
  result = ''
  i = str.find(start_str)
  sub = str[i: i+25]
  print(sub)
  start = False
  for l in sub:
      if l.isnumeric():
          start = True
          result += l
      if start == True and not l.isnumeric():
          break

  return result



# /groups/431943047263055/user/
# href="/groups/557295677987925/user/100013817049936/
index = 0

mylist = []


while True:
    index = str.find("groups/" + groupId, index)
    # print(index)
    result = getNumber(str[index: index + 50], "user")

    if result == user_id_stop:
        break

    if result not in mylist and result not in existIDs:
        mylist.append(result)
        # print(result)
        fo.write(result+"\n")

    if index == -1:
        break
    index += 1

fi.close()
fo.close()


