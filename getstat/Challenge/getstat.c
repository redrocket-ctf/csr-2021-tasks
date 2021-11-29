// gcc -Wall -Wextra -no-pie -O2 -o getstat getstat.c

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);

    printf("            _       _        _   \n"
           "           | |     | |      | |  \n"
           "  __ _  ___| |_ ___| |_ __ _| |_ \n"
           " / _` |/ _ \\ __/ __| __/ _` | __|\n"
           "| (_| |  __/ |_\\__ \\ || (_| | |_ \n"
           " \\__, |\\___|\\__|___/\\__\\__,_|\\__|\n"
           "  __/ |                          \n"
           " |___/                           \n\n\n");

    double x_quer = 0; // arithmetisches Mittel
    double s_quadrat = 0; // korrigierte Stichprobenvarianz

    size_t stichproben_groesse = 0;
    printf("Bitte Größe der Stichprobe eingeben: ");
    if (scanf("%zu", &stichproben_groesse) != 1)
        return 0;

    double werte[stichproben_groesse];
    for (size_t i = 0; i < stichproben_groesse; i++) {
        printf("Bitte Wert eingeben: ");
        if (scanf("%lf", &werte[i]) != 1)
            return 0;
    }

    for (size_t i = 0; i < stichproben_groesse; i++) {
        x_quer += werte[i];
    }
    x_quer /= stichproben_groesse;

    printf("Arithmetisches Mittel: %lf\n", x_quer);

    for (size_t i = 0; i < stichproben_groesse; i++) {
        double d = werte[i] - x_quer;
        s_quadrat += d * d;
    }
    s_quadrat /= stichproben_groesse - 1;

    printf("Korrigierte Stichprobenvarianz: %lf\n", s_quadrat);

    return 0;
}

void shell(void) {
    system("sh");
}
