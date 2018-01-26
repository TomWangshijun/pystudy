#include <iostream>
#include <string>
/*
两个数字2，3，请用户输入名称，然后猜第3个数字是多少。
输入后，对错都给出提示。
并询问是否继续。
最终给出分数。
*/
//Todo：这个应该可以用class再实现一次。
using namespace std;

int main()
{
    int result;             //输入的结果
    bool go_again = true;   //是否继续
    int right_times=0;      //答对次数
    float times=0;          //总计次数，因为/为整除，所以两个整数型，会导致结果为整数。
    string username;        //用户名
    char yesorno;           //是否继续，字符型

    cout << "Welcome to this game, what\'s your name?" << endl;
    cin >> username;
    while (go_again){       //go_again为false时退出，即用户选择不继续时退出。
        cout << "There are tow number 2 and 3, the next number is ?" << endl;
        cin >> result;
        if (5== result){    //答案正确
            right_times++;
            cout << "Great, your answer is right."<< endl;
        }
        else
        {
            cout << "Sorry, the answer is not " << result << endl;
        }
        times++;
        cout << "Do you wanna play again(Y/N)?";
        cin >> yesorno;
        if ('N' == yesorno || 'n'==yesorno) //输入N，n就退出。
            go_again = false;               //Todo:应该再判断输入是否为Y，y
    }
    float score;
    score=right_times/times*10;             //满分为10分，Todo：应提示。
    cout << "Well," << username << ", your score is " << score << ".\nGoodbye!" << endl;
    return 0;
}
