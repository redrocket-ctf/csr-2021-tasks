#include <fcntl.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
  int fd = open("/dev/null", O_WRONLY);
  if (fd == -1) {
    perror("Failed to open /dev/null\n");
    exit(1);
  }
  while (1) {
    char *secret = "CSR{https://www.youtube.com/watch?v=ClTS8qlhAx4}";
    char spambuffer[256];
    printf("Writing covert channel to /dev/null...\n");
    sleep(1);
    for (size_t i = 0; i < strlen(secret); ++i) {
      write(fd, spambuffer, secret[i]);
    }
  }
}