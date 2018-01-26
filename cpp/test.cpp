#include <iostream>
#include <string>

using namespace std;

int main()
{
    int result;
    bool go_again = true;
    int right_times=0;
    float times=0;
    string username;
    char yesorno;

    cout << "Welcome to this game, what\'s your name?" << endl;
    cin >> username;
    while (go_again){
        cout << "There are tow number 2 and 3, the next number is ?" << endl;
        cin >> result;
        if (5== result){
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
        if ('N' == yesorno || 'n'==yesorno)
            go_again = false;
    }
    float score;
    score=right_times/times;
    cout << "Well," << username << ", your score is " << score*10 << ".\nGoodbye!" << endl;
    return 0;
}
