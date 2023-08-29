The Solution
============
The project contains two projects. One project is a class library that contains code for a Concurrent Bimap. Unfortunately I haven't done a version for
a single thread that does not have thread safety baked in. Feel free to take the code and create a modified version suitable for single thread. I have
only seen a Bimap for C++ Boost. I have not seen a Bidirectional dictionary for .Net and I definitely haven't seen a thread safe Bimap.

This Bimap uses Slim Reader Writer locks so it is more suitable for application that require a Bimap within the same application process. It does not 
use full process Reader Writer Locks so it is not suitable for multi process synchronization. But I suspect this is not difficult to modify.

The second project is a demo console application that tests the Bimap using three threads.

Unfortunately I haven't had the time to write the Unit Tests. However I haven't had any problems and it does seem to be working. Feel free to provide
feedback and write your own unit tests.

The Console Demo Project
========================
I do realise that there is alot going on and it may be difficult to keep track of whats going on. Basically we create three tasks. The main tasks are
the adder task and the deleter task. We should be able to add to the Bimap if it is not contained in the Bimap. Note it will work because we have one
adder thread. Same is true for the deleter task. If it is in the Bimap (we work on one side either right or left) then we should be able to remove from
the Bimap. Either case we should be able to predict success or failure. Just keep track of the output in capital letters and we should be able to 
predict the operation whether it was successful or failure. We are just making the thread sleep just to simulate speed. 

As regards to the reader task it is just there to see if it can read from the Bimap and not affect the Deleter and adder. We should be able to allow
multiple readers at the same time but only one writer. We can also request a special upgradable write lock if we need to perform an update operation.

The main thing is our demo does not crash and we don't read any null values because we are trying to access the values through the Try methods. This
is why there are no indexers. We should use the Try methods to test the return value from the function to see if the operation succeeded. 

The enumerator methods should work because we are creating a copy of the whole dictionary and then returning a separate enumerator so when it a thread
is enumerating these values it is not guaranteed to be synchronized with the main Bimap.

I created this project years ago and had to remove the enable nullable tag in the project file because this was causing so many warnings.

Love to hear any feedback

duongchu@hotmail.com