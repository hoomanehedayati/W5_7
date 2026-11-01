
DELIMITER = ','
def collectWords():
  word=input("Insert word(empty stops): ")
  allwords=""
  while word != "":
    allwords+=word+DELIMITER
    word=input("Insert word(empty stops): ")
  return allwords  

def analyseWords(allwords):
  words=allwords.split(DELIMITER)
  words.remove("")
  wordamount=len(words)
  charamount=len(allwords)-wordamount
  print(f"- {wordamount} Words")
  print(f"- {charamount} Characters")
  print(f"{charamount/wordamount} Average word length")

def main():    
  print("Program starting.")
  words=collectWords()
  analyseWords(words)
  print("Program ending.")
main()  