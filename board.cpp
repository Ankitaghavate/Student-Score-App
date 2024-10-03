#include <iostream>
#include <unordered_map>
#include <set>
#include <string>

using namespace std;

struct User {
    int id;
    string name;
    
    User(int userId, string userName) : id(userId), name(userName) {}
};

class Leaderboard {
private:
    set<pair<int, int>> sortedScores;
    unordered_map<int, pair<string, int>> userMap;

public:
    void addUser(int userId, string name) {
        if (userMap.find(userId) != userMap.end()) {
            cout << "User already exists!" << endl;
            return;
        }
        userMap[userId] = {name, 0};
        sortedScores.insert({0, userId});
        cout << "User added: " << name << " with UserID: " << userId << endl;
    }

    void updateScore(int userId, int newScore) {
        if (userMap.find(userId) == userMap.end()) {
            cout << "User does not exist!" << endl;
            return;
        }

        int oldScore = userMap[userId].second;
        sortedScores.erase({oldScore, userId});
        userMap[userId].second = newScore;
        sortedScores.insert({newScore, userId});
        cout << "Score updated for UserID: " << userId << " to " << newScore << endl;
    }

    void getTopN(int N) {
        cout << "Top " << N << " users:\n";
        auto it = sortedScores.rbegin();
        for (int i = 0; i < N && it != sortedScores.rend(); ++i, ++it) {
            int userId = it->second;
            string name = userMap[userId].first;
            int score = it->first;
            cout << name << " (UserID: " << userId << ") - Score: " << score << endl;
        }
    }

    int getUserRank(int userId) {
        if (userMap.find(userId) == userMap.end()) {
            cout << "User does not exist!" << endl;
            return -1;
        }

        int rank = 1;
        int userScore = userMap[userId].second;

        for (auto it = sortedScores.rbegin(); it != sortedScores.rend(); ++it) {
            if (it->second == userId) break;
            rank++;
        }

        cout << "Rank of UserID: " << userId << " is " << rank << endl;
        return rank;
    }
};

int main() {
    Leaderboard leaderboard;
    int choice, userId, score, N;
    string name;

    while (true) {
        cout << "\n1. Add User\n";
        cout << "2. Update User Score\n";
        cout << "3. Get Top N Users\n";
        cout << "4. Get User Rank\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter User ID: ";
                cin >> userId;
                cout << "Enter User Name: ";
                cin >> name;
                leaderboard.addUser(userId, name);
                break;

            case 2:
                cout << "Enter User ID: ";
                cin >> userId;
                cout << "Enter new score: ";
                cin >> score;
                leaderboard.updateScore(userId, score);
                break;

            case 3:
                cout << "Enter N (number of top users to display): ";
                cin >> N;
                leaderboard.getTopN(N);
                break;

            case 4:
                cout << "Enter User ID: ";
                cin >> userId;
                leaderboard.getUserRank(userId);
                break;

            case 5:
                cout << "Exiting...\n";
                return 0;

            default:
                cout << "Invalid choice, please try again.\n";
        }
    }
    return 0;
}
