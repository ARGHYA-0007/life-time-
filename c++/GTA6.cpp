// gta6_fake_codegen.cpp
// Harmless fake "GTA6" code generator for cinematic overlays / mockups.
// Compile: g++ -std=c++17 -O2 -o gta6_fake_codegen gta6_fake_codegen.cpp

#include <bits/stdc++.h>
using namespace std;

static std::mt19937_64 rng((unsigned)chrono::high_resolution_clock::now().time_since_epoch().count());

string rand_chars(int len, bool letters=true, bool digits=true) {
    const string L = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const string D = "0123456789";
    string pool;
    if(letters) pool += L;
    if(digits) pool += D;
    if(pool.empty()) pool = D;
    uniform_int_distribution<size_t> dist(0, pool.size()-1);
    string s;
    for(int i=0;i<len;++i) s += pool[dist(rng)];
    return s;
}

string gen_fake_code() {
    // Example patterns: AAAA-BBBB-CCCC or 0000-XXXX-77YY
    vector<function<string()>> patterns = {
        [&](){ return rand_chars(4,true,false) + "-" + rand_chars(4,false,true) + "-" + rand_chars(4,true,true); },
        [&](){ return rand_chars(2,true,true) + rand_chars(2,false,true) + "-" + rand_chars(4,true,false) + "-" + rand_chars(4,true,true); },
        [&](){ return rand_chars(4,false,true) + "-" + rand_chars(4,false,true) + "-" + rand_chars(4,false,true); },
        [&](){ return rand_chars(3,true,true) + "-" + rand_chars(5,true,false) + "-" + rand_chars(3,false,true); }
    };
    uniform_int_distribution<size_t> d(0, patterns.size()-1);
    return patterns[d(rng)]();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cout << "GTA6 — FAKE CODE GENERATOR (for cinematic / overlay use only)\n";
    cout << "Enter how many codes to generate (1-100). Enter 0 to exit.\n";

    while(true){
        cout << "\nHow many codes? ";
        int n;
        if(!(cin >> n)) break;
        if(n <= 0) break;
        n = min(n, 100);
        cout << "\nGenerated codes:\n";
        for(int i=0;i<n;++i) {
            string code = gen_fake_code();
            cout << "  " << setw(2) << i+1 << ") " << code << "\n";
        }

        cout << "\nSave these to file? (y/N) ";
        char c; cin >> c;
        if(c=='y' || c=='Y') {
            string fname;
            cout << "Filename (default: fake_codes.txt): ";
            cin >> ws;
            getline(cin, fname);
            if(fname.empty()) fname = "fake_codes.txt";
            ofstream ofs(fname, ios::app);
            if(!ofs) {
                cerr << "Failed to open " << fname << " for writing.\n";
            } else {
                for(int i=0;i<n;++i) ofs << gen_fake_code() << "\n";
                ofs.close();
                cout << "Saved to " << fname << "\n";
            }
        }
    }

    cout << "Goodbye — use the codes only as fictional overlays or props.\n";
    return 0;
}
