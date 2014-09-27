/* Prototypes */

extern void flushall(int);
extern void timer_start(void);
extern void timer_stop(void);
extern double timer_elapsed(void);

/* Macros */

#define FLUSHALL(a) if (!noflush) flushall(a) 
#define TIMER_START timer_start()
#define TIMER_STOP timer_stop()
#define TIMER_ELAPSED timer_elapsed()

#define INLINE inline

#define REGISTER register

#ifdef DEBUG
#define DBG(a) a;
#else
#define DBG(a)
#endif

