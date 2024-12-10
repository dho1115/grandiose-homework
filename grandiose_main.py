from grandiose import FindSynonym, result;

if __name__ == '__main__':
   SynonymInput = input("Input a synonym for \"faster\": ");
   print(result(FindSynonym("function"), SynonymInput))
