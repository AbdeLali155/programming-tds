// 0 1 1 0 1
// 1 1 0 1 0
// 0 1 1 1 0
// 1 1 1 1 0
// 1 1 1 1 1
// 0 0 0 0 0   
#include <stdio.h>

void fonction(int T[][5],int i,int j){
    int max=0;
    int imax[2];
   for(int i=0;i<6;i++){
         for(int j=0;j<5;j++){
            if(T[i][j]==1){
                if(T[i][j+1]==1 && T[i+1][j]==1 && T[i+1][j+1]==1){
                    if(max<2){
                        max=2;
                        imax[0]=i; imax[1]=j;
                    }
                    if(T[i][j+2]==1 && T[i+2][j]==1 && T[i+1][j+2]==1 && T[i+2][j+1]==1 && T[i+2][j+2]==1){
                        if(max<3){
                        max=3;
                        imax[0]=i; imax[1]=j;
                        
                        } 
                        if(T[i][j+3]==1 && T[i+1][j+3]==1 && T[i+2][j+3]==1 && T[i+3][j]==1 && T[i+3][j+1]==1 && T[i+3][j+2]==1 && T[i+3][j+3]==1){
                            if(max<4){
                            max=4;
                            imax[0]=i; imax[1]=j;
                            } 
                            if(T[i][j+4]==1 && T[i+1][j+4]==1 && T[i+2][j+4]==1 && T[i+3][j+4]==1 && T[i+4][j+4]==1 && T[i+4][j+3]==1 && T[i+4][j+2]==1 && T[i+4][j+1]==1 && T[i+4][j]==1){
                                if(max<5){
                                max=5;
                                imax[0]=i; imax[1]=j;
                                } 
                            }
                        }
                    }
                }
            }
        }
    }


    printf("u need to start with point %d,%d and go %d step stright and %d down and finish the squer with dil3 equals %d this is ur square \n",imax[0],imax[1],max,max,max);
   for(int i=0;i<max;i++){
         for(int j=0;j<max;j++){
            printf("%d ",T[imax[0]+i][imax[1]+j]);
        }
        printf("\n");
    }
}
int main(){
    int T[6][5]={{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1}};
    fonction(T,6,5);
}