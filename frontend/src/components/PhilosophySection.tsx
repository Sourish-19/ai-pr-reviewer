import React, { useRef } from 'react';
import { motion, useInView } from 'framer-motion';

export default function PhilosophySection() {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-100px" });

  return (
    <section id="security" className="bg-black py-28 md:py-40 px-6 overflow-hidden flex justify-center">
      <div className="max-w-6xl w-full" ref={ref}>
        <motion.h2
          initial={{ opacity: 0, y: 40 }}
          animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 40 }}
          transition={{ duration: 0.8 }}
          className="text-5xl md:text-7xl lg:text-8xl text-white tracking-tight mb-16 md:mb-24"
        >
          Speed <em className="italic text-white/40 font-serif" style={{ fontFamily: "'Instrument Serif', serif" }}>x</em> Security
        </motion.h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12">
          <motion.div
            initial={{ opacity: 0, x: -40 }}
            animate={isInView ? { opacity: 1, x: 0 } : { opacity: 0, x: -40 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="rounded-3xl overflow-hidden aspect-[4/3]"
          >
            <video
              ref={(v) => { if(v) { v.defaultMuted = true; v.muted = true; v.playsInline = true; } }}
              className="w-full h-full object-cover"
              src="https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260307_083826_e938b29f-a43a-41ec-a153-3d4730578ab8.mp4"
              muted
              autoPlay
              loop
              playsInline
              preload="auto"
            />
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 40 }}
            animate={isInView ? { opacity: 1, x: 0 } : { opacity: 0, x: 40 }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="flex flex-col justify-center"
          >
            <div className="mb-10 md:mb-12">
              <div className="text-white/40 text-xs tracking-widest uppercase mb-4">
                Shift Left Security
              </div>
              <p className="text-white/70 text-base md:text-lg leading-relaxed">
                Waiting for CI/CD pipelines to catch basic syntax flaws is a waste of time. Run our CLI locally before you even push to catch errors instantaneously.
              </p>
            </div>

            <div className="w-full h-px bg-white/10 mb-10 md:mb-12" />

            <div>
              <div className="text-white/40 text-xs tracking-widest uppercase mb-4">
                Maintain Clean Code
              </div>
              <p className="text-white/70 text-base md:text-lg leading-relaxed">
                We believe pull requests should be insightful without bias. Let AI handle the formatting and basic checks while human reviewers focus on architecture.
              </p>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
