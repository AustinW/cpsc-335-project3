
#include <chrono>
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <sstream>

using namespace std;

void replace_this_with_a_real_algorithm() {
  // waste time...
  const int N = 1 << 15;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      ;
}

vector<string> ip_selection_sort(vector<string> L) {
    int n = L.size();

    for (int k = 0; k < n - 1; ++k) {
        int j = k;

        for (int i = (k + 1); i < n; ++i) {
//            cout << "i = " << i << " and j = " << j << " and k = " << k << endl;
            if (strcasecmp(L[i].c_str(), L[j].c_str()) < 0) {
                j = i;
            }
        }

//        cout << "Swapping k = " << k << " and j = " << j << endl;
        swap(L[k], L[j]);
    }

    return L;
}

void print_first_lines(vector<string> inp, int n) {
    for (int i = 0; i < n; ++i)
        cout << (i + 1) << ". " << inp[i] << endl;
}

int main(int argc, char** argv) {

    string filename;

    cout << "Specify a file to read (beowulf.txt): ";
    getline(cin, filename);

    if (filename == "" || filename == "\n") {
        filename = "beowulf.txt";
    }

    try {
        // 1. Load input file
        ifstream f(filename);

        // 2. Specify n to use
        int n;
        cout << "For what n? ";
        cin >> n;

        vector<string> L;

        int i = 0;
        string line;

        while (getline(f, line)) {
            if (i == n) break;

            L.push_back(line);

            ++i;
        }

        // Be a good citizen
        f.close();

        // 3. Print the first 10 words
        print_first_lines(L, 10);

        cout << "In place selection sort..." << endl;

        // Start the timer
        auto start = chrono::high_resolution_clock::now();

        // 4. Sort the first n words
        vector<string> sorted = ip_selection_sort(L);

        // Stop the timer
        auto end = chrono::high_resolution_clock::now();

        // 5. Measure running time
        int microseconds = chrono::duration_cast<chrono::microseconds>(end - start).count();
        double seconds = microseconds / 1E6;

        // 6. Print the first 10 words in sorted sequence
        cout << "Sorted:" << endl;
        print_first_lines(sorted, 10);

        // 7. Print the elapsed time
        cout << "Elapsed time: " << seconds << " seconds" << endl;

    } catch (ifstream::failure e) {
        cerr << "Error opening file";
        exit(EXIT_FAILURE);
    }

    return 0;
}
