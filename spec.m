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
interval = 0.5*start;
finish = N - mod(N, start) - interval;

m = zeros(start,finish);
j = 1;
for i = start:interval:finish
    w = s(i-interval:i+interval-1);
    u = fft(w);
    m(:,j) = abs(u);
    j = j + 1;
end
m = m(:, 1:interval);

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
interval = 0.5*start;
finish = N - mod(N, start) - interval;

m = zeros(start,finish);
j = 1;
for i = start:interval:finish
    w = s(i-interval:i+interval-1);
    u = fft(w);
    m(:,j) = abs(u);
    j = j + 1;
end
m = m(:, 1:interval);

imagesc(m);
set(gca,'YDir','normal')
axis on;
xticklabels(0.5:0.5:3.5);
yticklabels(1000:500:Fs/2);
title('Spectrogram');
xlabel('t(sec)');
ylabel('f(Hz');