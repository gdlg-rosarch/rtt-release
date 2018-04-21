/***************************************************************************
  tag: Peter Soetens  Sat May 7 12:56:51 CEST 2005  win32.h

                        win32.h -  description
                           -------------------
    begin                : Sat May 07 2005
    copyright            : (C) 2005 Peter Soetens
    email                : peter.soetens@mech.kuleuven.ac.be

 ***************************************************************************
 *   This library is free software; you can redistribute it and/or         *
 *   modify it under the terms of the GNU General Public                   *
 *   License as published by the Free Software Foundation;                 *
 *   version 2 of the License.                                             *
 *                                                                         *
 *   As a special exception, you may use this file as part of a free       *
 *   software library without restriction.  Specifically, if other files   *
 *   instantiate templates or use macros or inline functions from this     *
 *   file, or you compile this file and link it with other files to        *
 *   produce an executable, this file does not by itself cause the         *
 *   resulting executable to be covered by the GNU General Public          *
 *   License.  This exception does not however invalidate any other        *
 *   reasons why the executable file might be covered by the GNU General   *
 *   Public License.                                                       *
 *                                                                         *
 *   This library is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU     *
 *   Lesser General Public License for more details.                       *
 *                                                                         *
 *   You should have received a copy of the GNU General Public             *
 *   License along with this library; if not, write to the Free Software   *
 *   Foundation, Inc., 59 Temple Place,                                    *
 *   Suite 330, Boston, MA  02111-1307  USA                                *
 *                                                                         *
 ***************************************************************************/



/**
 * @file win32.h
 * This file indicates that the win32 version of
 * orocos headers is installed.
 */

// Include this windows stuff as soon as possible. We use LEAN_AND_MEAN because of the Winsock include madness

#ifndef _WIN32_WINNT
#define _WIN32_WINNT 0x400
#endif
# ifndef WIN32_LEAN_AND_MEAN
#  define WIN32_LEAN_AND_MEAN 
# endif
# ifndef NOMINMAX
#  define NOMINMAX
# endif
#  include <windows.h>
#  undef interface	// To avoid name clash with namespace interface and Windows SDK objbase.h
#  include <mmsystem.h> // For timeBeginPeriod()
#  include <winsock2.h>
#  include <ws2tcpip.h>
