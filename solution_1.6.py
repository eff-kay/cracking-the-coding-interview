def rotate(m):
    return zip(*m[::-1])
    
    
    
def main():
    print rotate([[1,2,3],[4,5,6],[7,8,9]])
    m=[[1,2],[3,4]]
    print rotate(m)
    
def __name__=='__main__':
    main()
