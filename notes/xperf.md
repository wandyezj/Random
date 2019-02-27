# Xperf

xperf -on Base+Cswitch+Virt_Alloc -stackwalk VirtualAlloc -BufferSize 1024 -MinBuffers 256 -MaxBuffers 256
xperf -start HeapSession -heap -Pids 0 -stackwalk HeapAlloc+HeapRealloc -BufferSize 1024 -MinBuffers 256 -MaxBuffers 256 -MaxFile 256
 
if you notice, above, there is a call out for “stackwalk” which will capture data, similar to office profiler, if you have symbols, will allow you to actually show stack trace information in the WPA.

There was an old tool that made this easier, so you didn’t have to look up settings called Xperf123.

https://archive.codeplex.com/?p=xperf123

There is a newer one called UIForETW.

https://github.com/google/UIforETW

https://randomascii.wordpress.com/2015/04/14/uiforetw-windows-performance-made-easier/

Additional References:

https://channel9.msdn.com/Events/Build/BUILD2011/HW-59T

https://wiki.mozilla.org/Tracing_VirtualAlloc_With_Xperf

Windows Performance Recorder (WPR) enables snapshot of heap for specific processes on the system