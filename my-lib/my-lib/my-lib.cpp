// my-lib.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"


extern "C"
{
  __declspec(dllexport) int my_cpp_function(wchar_t* arg1, const int(*callback_function(int, wchar_t*)))
  {
    // callback_function takes two arguments
    //    int      : moves the ArcGIS gp progressor from 0-100% in 10 steps
    //    wchar_t* : string added to the tool's messages
    // callback_function returns an int, either 1 (cancel) or 0 (continue)

    (int)callback_function(0, arg1); // pass arg1 back
    (int)callback_function(0, L"Message from dll (start of loop)");

    for (int i = 0; i < 10; i++)
    {
      if ((int)callback_function(i, L"") == 1)  // i will move the progress bar
        return 1; // if callback returned 1 the user has clicked 'cancel' so quit

      Sleep(1000);
    }

    (int)callback_function(0, L"Message from dll (end of loop)");

    return 0; // return 0 = success
  }

}