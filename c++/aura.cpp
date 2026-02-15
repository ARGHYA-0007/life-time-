#include <iostream>
#include <chrono>
#include <thread>
#include <cstdlib>

using namespace std;

void clearScreen() {
    // For Windows
    system("cls");
}

void printScene(int frame) {
    string aura = (frame % 2 == 0) ? "✨🔥🌾✨" : "🌟🌿🔥🌟";

    cout << "       " << aura << endl;
    cout << "      \\(^_^)/     <-- Farming Boy Dancing" << endl;
    cout << "       / | \\" << endl;
    cout << "        / \\" << endl;
    cout << "     ~~~~~~~~~~~~~" << endl;
    cout << "    ~  ~  ~ BOAT ~ ~" << endl;
    cout << "     ~~~~~~~~~~~~~" << endl;
    cout << "🌊 🌊 🌊 🌊 🌊 🌊 🌊 🌊 🌊" << endl;
}

int main() {
    for (int i = 0; i < 20; ++i) {
        clearScreen();
        printScene(i);
        std::this_thread::sleep_for(std::chrono::milliseconds(500));  // ✅ Correct usage
    }

    cout << "\nDANCE FINISHED 🚤✨\n";
    return 0;
}



