[s,Fs] = audioread('sample.wav');
sound(s,Fs)
%%
N = length(s)
Fs
T = N/Fs
%%
a = 400;
b = 800;
c = 1199;

w = s(a:c);
Nw = length(w)
u = fft(w);
t = (0:Nw-1)*Fs/Nw
length(t)
plot(t, real(u))
title("Real")
plot(t, imag(u))
title("Imag")
plot(t, abs(u))
title("Magnitude")
%%
start = Fs * 0.1;
interval = Fs * 0.1;
overlap = 0.05 * Fs;
numWindows = round(((N - start) / ( 0.5 * interval)) - 1);
m = zeros(interval, numWindows);

for i = 1:numWindows
    w = s(start : start + interval - 1);                                                                                                           
    u = fft(w);                                                                         
    m(:,i) = abs(u);
    start = start + interval - overlap;
 
end

imagesc(m);
set(gca,'YDir','normal')
axis on;
xticklabels(0.5:0.5:3.5);
yticklabels(1000:500:4000);
title('Spectrogram');
xlabel('t(sec)');
ylabel('f(Hz');
%%
[s,Fs] = audioread('File5.wav');
%%
N = length(s)
Fs
T = N/Fs
%%
a = 400;
b = 800;
c = 1199;

w = s(a:c);
Nw = length(w)
u = fft(w);
t = (0:Nw-1)*Fs/Nw
length(t)
plot(t, real(u))
title("Real")
plot(t, imag(u))
title("Imag")
plot(t, abs(u))
title("Magnitude")
start = Fs * 0.1;
interval = Fs * 0.1;
overlap = 0.05 * Fs;
numWindows = round(((N - start) / ( 0.5 * interval)) - 1);
m = zeros(interval, numWindows);

for i = 1:numWindows
    w = s(start : start + interval - 1);                                                                                                           
    u = fft(w);                                                                         
    m(:,i) = abs(u);
    start = start + interval - overlap;
 
end

imagesc(m);
set(gca,'YDir','normal')
axis on;
xticklabels(0.5:0.5:3.5);
yticklabels(1000:500:4000);
title('Spectrogram');
xlabel('t(sec)');
ylabel('f(Hz');