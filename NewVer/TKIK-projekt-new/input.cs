int a = 8;
string n = "kk";

int funkcja(int b){
    return b;
}

class Klasa1{
    char x = "k";
    int y = 10;
    double z = 0.1;

    int fwc(int i){
        if(i==5){
            return 1;
        }
        else{
            return y;
        }
    }

    double modulo(int i){
        return i%2;
    }

    double multiply(){
        return z*y;
    }

    int divide(){
        return y/z;
    }
}

class Klasa2{
    int i = 0;
    bool j = true;

    void fun1(int a){
        for(int i=0;i<=a;i+=1) {
            a +=1;
        }
    }

    void fun2(){
        string nazwa = 'nazwa';
        while(j) {
            i+=1;
        }
    }
}
