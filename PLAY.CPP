/* *************************
 * Use Turbo C++ to compile.
 * Copy the Python outputs 
 * and save as "TMP.H" at
 * the same directory of 
 * this CPP file.
 * *************************/

#include <dos.h>
#include <iostream.h>
#include "tmp.h"

int main() {
	int i = 0, j = 0;
	for (i=0; i<=NOTESCONUT; i++) {
		cout<<k[i][0]<<" ";
		for (j=0; j<=k[i][1]; j++) {
			sound(k[i][0]);
			delay(1);
		}
		nosound();
		delay(10);
	}
	nosound();
	return 0;
}
