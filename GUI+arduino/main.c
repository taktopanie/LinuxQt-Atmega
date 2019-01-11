/*
 * MAIN_Gui+arduino.c
 *
 *  Created on: 18 lis 2018
 *      Author: macko
 */


/* PROGRAM ��CZ�CY MIKROKONTROLER Z KOMPUTEREM ZA POMOC� UART
*/

#include<avr/io.h>
#include<avr/interrupt.h>
#include<util/delay.h>
#include<string.h>
#include<stdlib.h>
#include"Biblioteki/UART_obsluga.h"
#include"Biblioteki/Odkodowywanie.h"
#include"Biblioteki/SoftwarePWM.h"

//definicje zmiennych

#define SCK 16000000

volatile uint8_t stan;
uint8_t stan1;

// ZMIENNA (DO TESTU) SLUZACA DO WYSWIETLANIA KOMUNIKATOW PO WYKONANYCH DZIALANIACH
int wersja_testowa=0;

char tmp_zdanie[25];
char zdanie[25];

//extern struct KOD rozpoznawanie(char* zdanie);
volatile struct KOD struktura; //= rozpoznawanie("#00*00-00/000+");

float pomiar (int);

int main (void){

///////////////////////////////////////////////// CZYNNOSCI WSTEPNE////////////////////////////
// Pin PB0/PB1/PB2/B3 jako wyjscie dla diod

DDRB|=(1<<PB0)|(1<<PB1)|(1<<PB2)|(1<<PB3);

PORTB&=~(1<<PB0)&~(1<<PB1)&~(1<<PB2)&~(1<<PB3);
// Pin PB1 DLA PRZEKAZNIKA
//DDRB|=(1<<PB1);
//PORTB|=(1<<PB1);


//napiecie referencyjne 5v z mikrokontrolera
	ADMUX|=(1<<REFS0);
// wlaczenie ADC i ustawienie preskalera
	ADCSRA|=(1<<ADEN)|(1<<ADPS1)|(1<<ADPS2);

	DDRC|=(1<<PC0);
	PORTC&=~(1<<PC0);

char tmp_zmienna;
inicjacja_usart();

// URUCHOMIENIE PWM
DDRD|=(1<<PD5);
DDRD|=(1<<PD6);

TCCR0A |=(1<<WGM00);//Tryb fast PWM
TCCR0A |=(1<<WGM01);//Tryb fast PWM
//TCCR0B |=(1<<WGM02);//Tryb fast PWM

TCCR0A |=(1<<COM0A1);//Clear OC0A on Compare Match, set OC0A at BOTTOM (non-inverting mode)
TCCR0A |=(1<<COM0B1);//Clear OC0B on Compare Match, set OC0B at BOTTOM, (non-inverting mode)

TCCR0B |=(1<<CS01)|(1<<CS00);//preskaler 64 czyli (16 000 000/64)
//OCR0A=100;// maksymalny zabkres od 0 do OCR0A czyli (0-1000) 1kHz    zmiana stanu gdy osiegnie OCR0B


////////////////////////////////////////////////////////////////////////////////////////////////
while(1){

// pobranie zmiennej z bufora UART
tmp_zmienna = GET_BYTE();
static int i = 0;
	if(tmp_zmienna){

		if(tmp_zmienna =='+'){

			struktura = rozpoznawanie("#00*00-00/000+");

			// SPRAWDZENIE POPRAWNOSCI BUDOWY KODU
			if(tmp_zdanie[0] == '#'&& tmp_zdanie[3]=='*'&&tmp_zdanie[6]=='-'&&tmp_zdanie[9]=='/')
				struktura = rozpoznawanie(tmp_zdanie);

			/* WYBOR FUNKCJI ###############################
			 *
			 * 1 - zmiana pinow
			 * 2 - pomiar ADC
			 * 3 - generowanie PWM
			 */
			switch (struktura.funkcja){
			case 1:
				if(wersja_testowa)
				WYSYLANIE_TEXTU("CASE 1");
				// RESET PINOW
				if (struktura.pin==0){
					if(struktura.stan == 0){
					if(wersja_testowa)
					WYSYLANIE_TEXTU("RESET FUNKCJI 1");
					PORTB&=~(1<<PB0)&~(1<<PB1);
					}else if(struktura.stan == 1){
					if(wersja_testowa)
					WYSYLANIE_TEXTU("RESET FUNKCJI 2");
					PORTB&=~(1<<PB2)&~(1<<PB3);
					}

					}

				// PIN 1
				if (struktura.pin==1){
					if(wersja_testowa)
					WYSYLANIE_TEXTU("PIN 1");
					if(struktura.stan == 0){
						if(wersja_testowa)
						WYSYLANIE_TEXTU("STAN 0");
						PORTB&=~(1<<PB0);
					}else if(struktura.stan ==1){
						if(wersja_testowa)
						WYSYLANIE_TEXTU("STAN 1");
						PORTB|=(1<<PB0);
					}
				}
				// PIN 2
				if (struktura.pin==2){
					if(wersja_testowa)
					WYSYLANIE_TEXTU("PIN 2");
					if(struktura.stan == 0){
						if(wersja_testowa)
						WYSYLANIE_TEXTU("STAN 0");
						PORTB&=~(1<<PB1);
					}else if(struktura.stan ==1){
						if(wersja_testowa)
						WYSYLANIE_TEXTU("STAN 1");
						PORTB|=(1<<PB1);
					}
				}
				// PIN 3
				if (struktura.pin==3){
					if(wersja_testowa)
					WYSYLANIE_TEXTU("PIN 3");
					if(struktura.stan == 0){
						if(wersja_testowa)
						WYSYLANIE_TEXTU("STAN 0");
						PORTB&=~(1<<PB2);
					}else if(struktura.stan ==1){
						if(wersja_testowa)
						WYSYLANIE_TEXTU("STAN 1");
						PORTB|=(1<<PB2);
					}
				}
				// PIN 4
				if (struktura.pin==4){
					if(wersja_testowa)
					WYSYLANIE_TEXTU("PIN 4");
					if(struktura.stan == 0){
						if(wersja_testowa)
						WYSYLANIE_TEXTU("STAN 0");
						PORTB&=~(1<<PB3);
					}else if(struktura.stan ==1){
						if(wersja_testowa)
						WYSYLANIE_TEXTU("STAN 1");
						PORTB|=(1<<PB3);
									}
								}
				break;

			case 2:
				if(wersja_testowa)
				WYSYLANIE_TEXTU("CASE 2");
				double wartosc_pomiaru = pomiar(0);
				wartosc_pomiaru=wartosc_pomiaru*5/1024;
				char zmienna_do_wysw[2];
				dtostrf(wartosc_pomiaru,2,2,zmienna_do_wysw);
				WYSYLANIE_TEXTU("P");
				WYSYLANIE_TEXTU(zmienna_do_wysw);
				WYSYLANIE_TEXTU("\n");
				break;
			case 3:
				if(struktura.pin==5)
					Software_PWM(struktura.stan,struktura.wypelnienie);
				//	OCR0B=(255*struktura.wypelnienie/100);
				else if(struktura.pin==6)
					Software_PWM(5,struktura.wypelnienie);
				//		OCR0A=(255*struktura.wypelnienie/100);
				break;
			default:
				if(wersja_testowa)
				WYSYLANIE_TEXTU("DEFAULT");
				break;
			}

			i=0;

				// WYZEROWANIE ZMIENNYCH ZDANIE ABY ZAPISAC JA KOLEJNYMI DANYMI
				int n;
				for(n = 0; n<25; n++)
				{
					tmp_zdanie[n]=0;
					zdanie[n]=0;
				}

			// DODAWANIE ZMIENNEJ DO ZDANIA
			}else{
			tmp_zdanie[i]=tmp_zmienna;
			i++;
			}
		}
	}
}


float pomiar (int ch){
			// zapis ktorego kanalu chce uzyc
			ADMUX = (ADMUX & 0xF8) | ch;
			// start pomiaru
			ADCSRA |=(1<<ADSC);
			//dopoki nie zwroci 0
			while(ADCSRA & (1<<ADSC));
			return ADCW;
	}
