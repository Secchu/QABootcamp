namespace ConcurrentBimap
{
    public class RwBidictionary<R, L>
    {
        private ReaderWriterLockSlim lockSlim;
        private Dictionary<R, L> Right;
        private Dictionary<L, R> Left;

        public RwBidictionary()
        {
            Right = new Dictionary<R, L>();
            Left = new Dictionary<L, R>();
            lockSlim = new ReaderWriterLockSlim();
        }

        public RwBidictionary(IEqualityComparer<R> rightComparer)
        {
            Right = new Dictionary<R, L>(rightComparer);
            Left = new Dictionary<L, R>();
            lockSlim = new ReaderWriterLockSlim();
        }

        public RwBidictionary(IEqualityComparer<L> leftComparer)
        {
            Right = new Dictionary<R, L>();
            Left = new Dictionary<L, R>(leftComparer);
            lockSlim = new ReaderWriterLockSlim();
        }

        public RwBidictionary(IEqualityComparer<R> rightComparer, IEqualityComparer<L> leftComparer)
        {
            Right = new Dictionary<R, L>(rightComparer);
            Left = new Dictionary<L, R>(leftComparer);
            lockSlim = new ReaderWriterLockSlim();
        }

        public bool TryAdd(R mapping, L item)
        {
            try
            {
                lockSlim.EnterUpgradeableReadLock();
                if (Right.ContainsKey(mapping) || Left.ContainsValue(mapping))
                    return false;
                if (Right.ContainsValue(item) || Left.ContainsKey(item))
                    return false;

                lockSlim.EnterWriteLock();
                Right.Add(mapping, item);
                Left.Add(item, mapping);
                lockSlim.ExitWriteLock();

                return true;

            }
            finally
            {
                if (lockSlim.IsUpgradeableReadLockHeld)
                    lockSlim.ExitUpgradeableReadLock();
            }
        }

        public bool TryGetRightValue(R key, out L val)
        {
            try
            {
                val = default(L);
                lockSlim.EnterReadLock();
                if (!Right.ContainsKey(key))
                    return false;
                val = Right[key];

                return true;

            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

        public bool TryRemoveByRightKey(R rightKey)
        {
            try
            {
                lockSlim.EnterUpgradeableReadLock();
                if (Right.ContainsKey(rightKey))
                {
                    lockSlim.EnterWriteLock();
                    L leftKey = Right[rightKey];
                    Right.Remove(rightKey);

                    Left.Remove(leftKey);

                    lockSlim.ExitWriteLock();

                    return true;
                }

                return false;

            }
            finally
            {
                if (lockSlim.IsUpgradeableReadLockHeld)
                    lockSlim.ExitUpgradeableReadLock();
            }
        }

        public bool TryRemoveByLeftKey(L leftKey)
        {
            try
            {
                lockSlim.EnterUpgradeableReadLock();
                if (Left.ContainsKey(leftKey))
                {
                    lockSlim.EnterWriteLock();
                    R rightKey = Left[leftKey];
                    Left.Remove(leftKey);

                    Right.Remove(rightKey);

                    lockSlim.ExitWriteLock();

                    return true;
                }

                return false;

            }
            finally
            {
                if (lockSlim.IsUpgradeableReadLockHeld)
                    lockSlim.ExitUpgradeableReadLock();
            }
        }

        public object SyncRoot => lockSlim;

        public bool IsSynchronized => true;

        public int ActiveReaderCount => lockSlim.CurrentReadCount;

        public bool IsWriterActive => lockSlim.IsWriteLockHeld;

        public bool IsRwLockHeld => lockSlim.IsReadLockHeld;

        public bool TryGetLeftValue(L key, out R val)
        {
            try
            {
                val = default(R);
                lockSlim.EnterReadLock();
                if (!Left.ContainsKey(key))
                    return false;
                val = Left[key];

                return true;

            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }
        
        //For the Enumerators we will create a copy of the dictionary. This is expensive.
        //The values are not guaranteed to be synchronized. Concepts is similar to some databases
        //where the value you read from the database could be updated from a second connection
        //causing synchronization issues.
        public Dictionary<L, R>.Enumerator getLeftDictionaryEnumerator()
        {
            try
            {
                lockSlim.EnterReadLock();
                Dictionary<L, R> duplicate = new Dictionary<L, R>(Left);

                return duplicate.GetEnumerator();

            }
            finally
            {
                lockSlim.ExitReadLock();
            }
        }

        public Dictionary<R, L>.Enumerator GetRightDictionaryEnumerator()
        {
            try
            {
                lockSlim.EnterReadLock();
                Dictionary<R, L> duplicate = new Dictionary<R, L>(Right);

                return duplicate.GetEnumerator();

            }
            finally
            {
                lockSlim.ExitReadLock();
            }
        }

        public bool Contains(R mapping)
        {
            try
            {
                lockSlim.EnterReadLock();
                if (!Right.ContainsKey(mapping))
                    return false;

                return true;
            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

        public bool Contains(L mapping)
        {
            try
            {
                lockSlim.EnterReadLock();
                if (!Left.ContainsKey(mapping))
                    return false;

                return true;
            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

        public R[] RightKeys()
        {
            R[] keys = null;

            try
            {
                lockSlim.EnterReadLock();
                if (Right.Count == 0)
                    return null;

                keys = new R[Right.Count];
                Right.Keys.CopyTo(keys, 0);

                return keys;

            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

        public L[] LeftKeys()
        {
            L[] keys = null;

            try
            {
                lockSlim.EnterReadLock();
                if (Left.Count == 0)
                    return null;

                keys = new L[Left.Count];
                Left.Keys.CopyTo(keys, 0);

                return keys;

            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

        public bool ContainsRightKey(R mapping)
        {
            try
            {
                lockSlim.EnterReadLock();
                if (!Right.ContainsKey(mapping))
                    return false;

                return true;
            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

        public bool ContainsLeftKey(L mapping)
        {
            try
            {
                lockSlim.EnterReadLock();
                if (!Left.ContainsKey(mapping))
                    return false;

                return true;
            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

        public bool ContainsRightValue(L mapping)
        {
            try
            {
                lockSlim.EnterReadLock();
                if (!Right.ContainsValue(mapping))
                    return false;

                return true;
            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

        public bool ContainsLeftValue(R mapping)
        {
            try
            {
                lockSlim.EnterReadLock();
                if (!Left.ContainsValue(mapping))
                    return false;

                return true;
            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }



        public bool TryUpdate(R rightKey, R updatedRight, L updatedLeft)
        {
            try
            {
                lockSlim.EnterWriteLock();

                if (!Right.ContainsKey(rightKey))
                    return false;

                L mapping = Right[rightKey];
                Right.Remove(rightKey);
                Left.Remove(mapping);

                if (Right.ContainsKey(updatedRight) || Left.ContainsKey(updatedLeft))
                {
                    Right.Add(rightKey, mapping);
                    Left.Add(mapping, rightKey);
                    return false;
                }

                Right.Add(updatedRight, updatedLeft);
                Left.Add(updatedLeft, updatedRight);

                return true;

            }
            finally
            {
                if (lockSlim.IsWriteLockHeld)
                    lockSlim.ExitWriteLock();
            }
        }

        public Dictionary<R, L>.Enumerator RightEnumerator()
        {
            try
            {
                lockSlim.EnterReadLock();
                Dictionary<R, L> RightCopy = new Dictionary<R, L>(Right);

                return RightCopy.GetEnumerator();

            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

        public int Count
        {
            get
            {
                try
                {
                    lockSlim.EnterReadLock();
                    return Right.Count;

                }
                finally
                {
                    if (lockSlim.IsReadLockHeld)
                        lockSlim.ExitReadLock();
                }
            }
        }

        public Dictionary<L, R>.Enumerator LeftEnumerator()
        {
            try
            {
                lockSlim.EnterReadLock();
                Dictionary<L, R> LeftCopy = new Dictionary<L, R>(Left);

                return LeftCopy.GetEnumerator();

            }
            finally
            {
                if (lockSlim.IsReadLockHeld)
                    lockSlim.ExitReadLock();
            }
        }

    }
}