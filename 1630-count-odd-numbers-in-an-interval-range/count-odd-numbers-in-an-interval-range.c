int countOdds(int low, int high){
    int i,count=0;
    for(i=low;i<=high;i++)
    {
        if(i%2!=0)
        {
            count+=1;
        }
    }
    return count;

}