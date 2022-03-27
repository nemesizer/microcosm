/*
  microcosm.c - C conversion of the BASIC program.

  Jason Hood, 4 May, 1998.

  Revised 2 January & 13 March, 2006.
  Revised 18 January, 2009.

  22 January, 2009:
    put the keys in the same order as the GUI version;
    select key by page (add nondigit for other key), keyring keys by negative;
    don't bother with text, just accept the numbers;
    reads state.txt (or command line file), but doesn't write it;
    accepts line numbers and key number from the command line.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#else
#include <conio.h>
#endif


int  m[20];
char a[14][30];
char x[30];
int  i, j;

#include "text.h"

const char* const keys[] =
{
/*  1 */ "EUJGZBBEIKUVQFQCGKNQ", // L8
/*  1 */ "JBFCEGMQREYHBVHNLVZP", // L13
/*  2 */ "DUJJTWNDXAGTBKMJVTMD", // L11
/*  3 */ "VMHOKWMIZWKZTJDYFKSG", // L1
/*  4 */ "EKSYCFHEQTWUBEBTELCO", // L13
/*  5 */ "XBNVKXBPNGCYQSIUPJLV", // L5
/*  6 */ "KJYQKGAWZYAGVEJVKGUK", // L2
/*  7 */ "IVYIZJJOLFOGQOPJJEXY", // L14
/*  7 */ "EGEQOIOTFADVVJNNSGDL", // L5
/*  8 */ "ZGTEVNDRXKOSNHIHAEMU", // L3
/*  9 */ "TFRQAMYUWOLXKTDNBHIW", // L1
/* 10 */ "CPMVGKHPMEGPIDHQFJDF", // L9
/* 11 */ "WYTAPRVJHYHUJLTUTMVZ", // L5
/* 11 */ "JLIFDEPEKIUTCRBLWRLG", // L10
/* 12 */ "BKXKWEBUZOXSZCIFLAYC", // L7
/* 13 */ "PPRBIMCYJVRLKVXPUUGF", // L11

  // The keys on the keyring.
  "HMTFSDTGQJCIAZLDDCWB",
  "APYHZHJMCWURMHPFWVIK",
  "JQQZOZRUZPZRQSHBUQJE",
  "FZYMVFQGZOKDLJMIMPGQ",
  "HTJXDUFPLITWUYLCLTSO",
};

int key_map[] = { 0, 0, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15 };


void print_data( void );
void print_message( void );


#ifdef _WIN32
void clrscr( void )
{
  static BOOL	first = TRUE;
  static HANDLE hConOut;
  static COORD	pos;
  static DWORD	len;

  if (first)
  {
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    hConOut = GetStdHandle( STD_OUTPUT_HANDLE );
    for (len = 0; len < 21; ++len)
      putchar( '\n' );
    GetConsoleScreenBufferInfo( hConOut, &csbi );
    len = 21 * csbi.dwSize.X;
    pos.Y = csbi.dwCursorPosition.Y - 21;
    SetConsoleCursorPosition( hConOut, pos );
    first = FALSE;
  }
  else
  {
    DWORD written;
    SetConsoleCursorPosition( hConOut, pos );
    FillConsoleOutputCharacter( hConOut, ' ', len, pos, &written );
  }
}
#endif


int main( int argc, char* argv[] )
{
  int p;
  FILE* file;
  char* end;

  if (argc > 1 && (!strcmp( argv[1], "/?" ) || !strcmp( argv[1], "--help" )))
  {
    puts( "Microcosm by Hal Gashtan.\n"
	  "This program by Jason Hood <jadoxa@yahoo.com.au>.\n"
	  "http://ucosm.adoxa.cjb.net/\n"
	  "\n"
	  "ucosm [FILE]\n"
	  "ucosm PAGE1-LINE PAGE2-LINE ... PAGE13-LINE KEY" );
    return 0;
  }

  if (argc == 1)
  {
    for (i = 0; i < 13; ++i)
    {
      a[i][0] = "TYPE IN LINES"[i];
      a[i][1] = '\0';
    }
    strcpy( a[13], "NDOUSNNWQQWNKCUPXOZQ" );
  }
  else
  {
    file = fopen( argv[1], "r" );
    if (file)
    {
      for (i = 0; i < 13; ++i)
      {
	fscanf( file, "%d", &p );
	strcpy( a[i], pages[i][p] );
      }
      fscanf( file, "%d", &p );
      strcpy( a[13], keys[p] );
      fclose( file );
    }
    else
    {
      for (i = 0; i < 13; ++i)
      {
	p = (i+1 < argc) ? atoi( argv[i+1] ) : 0;
	if (p == 0 || p > 16)
	  p = 1;
	strcpy( a[i], pages[i][p-1] );
      }
      p = (i+1 < argc) ? strtol( argv[i+1], &end, 10 ) : 0;
      if (p == 0 || p > 13 || p < -5)
	strcpy( a[13], keys[0] );
      else if (p < 0)
	strcpy( a[13], keys[15-p] );
      else
      {
	if (*end)
	{
	  if (p == 1)
	    p = 1;
	  else if (p == 7)
	    p = 8;
	  else if (p == 11)
	    p = 13;
	  else
	    p = key_map[p];
	}
	else
	  p = key_map[p];
	strcpy( a[13], keys[p] );
      }
    }
  }

  for (;;)
  {
    clrscr();

    print_data();
    print_message();

    printf( "\nEnter Page:\t" );
    fflush( stdout );
    fgets( x, 30, stdin );
    p = atoi( x );
    if (p < 0)
      break;
    if (p == 0 || p > 14)
      p = 14;
    --p;
    printf( (p == 13) ? "Enter Key:\t" : "Enter Text:\t" );
    fflush( stdout );
    fgets( x, 30, stdin );
    j = strtol( x, &end, 10 );
    if (j)
    {
      if (p == 13)
      {
	if (j >= 1 && j <= 13)
	{
	  if (*end != '\n')
	  {
	    if (j == 1)
	      j = 1;
	    else if (j == 7)
	      j = 8;
	    else if (j == 11)
	      j = 13;
	    else
	      j = key_map[j];
	  }
	  else
	    j = key_map[j];
	  strcpy( a[p], keys[j] );
	}
	else if (-j >= 1 && -j <= 5)
	  strcpy( a[p], keys[15-j] );
      }
      else
      {
	if (j >= 1 && j <= 16)
	  strcpy( a[p], pages[p][j-1] );
      }
    }
  }

  return 0;
}


void print_data( void )
{
  printf( "Page\t\tText\n\n" );
  for (i = 0; i < 13; ++i)
    printf( " %2d\t\t%s\n", i+1, a[i] );
  printf( "\nKey\t\t%s\n", a[13] );
}


void print_message( void )
{
  int n;
  int c;

  memset( m, 0, sizeof(m) );
  printf( "Message\t\t" );
  n = 0;
  for (i = 0; i < 14; ++i)
  {
    for (j = 0; a[i][j]; ++j)
    {
      m[n] += a[i][j];
      if (++n == 20)
	n = 0;
    }
  }
  for (i = 0; i < 20; ++i)
  {
    c = (m[i] % 26) - 26 + 'Z';
    putchar( (c == '@') ? ' ' : c );
  }
  putchar( '\n' );
}