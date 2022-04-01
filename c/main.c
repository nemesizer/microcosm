#include "stdlib.h"
#include <string.h>
#include "stdio.h"

#define KEY_LENGTH 20
#define NUM_LINES 14

#define CORPUS_DIR = "/home/joseph/nltk_data/corpora/words/en"

typedef char Key[KEY_LENGTH];

struct key_pair {
    const char key[KEY_LENGTH];
    const int L;
};

struct key_pair keys[] = {
    {"EUJGZBBEIKUVQFQCGKNQ", 8},
    {"JBFCEGMQREYHBVHNLVZP", 13},
    {"DUJJTWNDXAGTBKMJVTMD", 11},
    {"VMHOKWMIZWKZTJDYFKSG", 1},
    {"EKSYCFHEQTWUBEBTELCO", 13},
    {"XBNVKXBPNGCYQSIUPJLV", 5},
    {"KJYQKGAWZYAGVEJVKGUK", 2},
    {"IVYIZJJOLFOGQOPJJEXY", 14},
    {"EGEQOIOTFADVVJNNSGDL", 5},
    {"ZGTEVNDRXKOSNHIHAEMU", 3},
    {"TFRQAMYUWOLXKTDNBHIW", 1},
    {"CPMVGKHPMEGPIDHQFJDF", 9},
    {"WYTAPRVJHYHUJLTUTMVZ", 5},
    {"JLIFDEPEKIUTCRBLWRLG", 10},
    {"BKXKWEBUZOXSZCIFLAYC", 7},
    {"PPRBIMCYJVRLKVXPUUGF", 11}
};

int contains_words (char* msg) {
    return 0;
}

char* gen_message(int m[20], int offset) {
    char message[20];

    for (int i = 0; i < 20; i++) {
        m[i] %= 26;
        while (m[i] > 0) {
            m[i] -= 26;
        }
        m[i] += 122;
        if (m[i] == 122) {
            message[i] = ' ';
        } else {
            message[i] = m[i];
        }
    }
}

void solve_lines_key(Key lines[NUM_LINES], Key key, int offset) {

    strcpy(lines[NUM_LINES-1], key);

    int n = 0;
    int m[20];

    for (int i = offset;;i++) {
        if (i >= ((sizeof lines) / (sizeof (char*)))) i = 0;

        char* line = lines[i];
        for (int j = 0; j < KEY_LENGTH; j++) {
            m[n] += line[j];
            n += 1;
            if (n == 20) n = 0;
        }

        if (i == offset-1) break;
    }

    char* message = gen_message(m, offset);

    if (contains_words(message)) {
        printf("*************");
        printf(lines);
        printf(key);
        printf(message);
        printf("*************");
    }

    free(message);
}

void solve_key(struct key_pair key) {

}

int main(int argc, char* argv[] ) {

}
