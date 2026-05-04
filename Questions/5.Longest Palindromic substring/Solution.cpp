#include <iostream>
#include <string>

std::string longestPalindrome(std::string s) {
    int n = s.size();
    int start = 0, len = 0;

    for (int i = 0; i < 2 * n - 1; i++) {
        int left = i / 2, right = (i + 1) / 2;
        while (left >= 0 && right < n && s[left] == s[right]) {
            left--;
            right++;
        }
        if (right - left - 1 > len) {
            start = left + 1;
            len = right - left - 1;
        }
    }
    
    return s.substr(start, len);
}

int main() {

    return 0;
}