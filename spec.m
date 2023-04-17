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
m = zeros(800,305200);
j = 1;
for i = 800:400:305200
    w = s(i-400:i+399);
    Nw = length(w);
    u = fft(w);
    m(:,j) = abs(u);
    j = j + 1;
end
m = m(:, 1:400);

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
m = zeros(800,27600);
j = 1;
for i = 800:400:27600
    w = s(i-400:i+399);
    Nw = length(w);
    u = fft(w);
    m(:,j) = abs(u);
    j = j + 1;
end
m = m(:, 1:400);

imagesc(m);
set(gca,'YDir','normal')
axis on;
xticklabels(0.5:0.5:3.5);
yticklabels(1000:500:4000);
title('Spectrogram');
xlabel('t(sec)');
ylabel('f(Hz');