/* *************************
 * Use TCC to compile instead
 * of GCC.
 * Copy the Python outputs 
 * and save as "TMP.H" at
 * the same directory of 
 * this CPP file.
 * *************************/

#include <sys/ioctl.h>
#include <unistd.h>
#include <linux/kd.h>
#include <stdio.h>
#include "tmp.h"

int main() {
	int i = 0;
	for (i=0; i<=NOTESCONUT; i++) {
		printf("%d ", k[i][0]);
		ioctl(STDOUT_FILENO, KIOCSOUND, k[i][0] == 0 ? 0 : 1193180/k[i][0]);
		usleep(k[i][1] * 1000);
		ioctl(STDOUT_FILENO, KIOCSOUND, 0);
		usleep(10000);
	}
	ioctl(STDOUT_FILENO, KIOCSOUND, 0);
	return 0;
}
