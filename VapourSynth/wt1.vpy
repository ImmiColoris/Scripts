import vapoursynth as vs
import havsfunc as haf
core = vs.get_core()

#load video
clip = core.lsmas.LWLibavSource(source="D:\\encode\\in\\wt1.mkv")
clip = haf.QTGMC(clip, Preset="Very Slow",TFF=True)
clip = core.std.SelectEvery(clip=clip, cycle=2, offsets=0)
clip = core.f3kdb.Deband(clip,dither_algo=2,output_depth=10)
clip = core.resize.Spline36(clip,1280,720)
clip.set_output()