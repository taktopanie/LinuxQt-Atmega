/*
 * SoftwarePWM.h
 *
 *  Created on: 15 lis 2018
 *      Author: Maciej Zwolan
 */

#ifndef SOFTWAREPWM_H_
#define SOFTWAREPWM_H_

extern volatile int licznik;
extern int wypelnienie;
extern int czestotliwosc;

void Software_PWM (int,int);



#endif /* SOFTWAREPWM_H_ */
