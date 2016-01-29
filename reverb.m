function y = reverb(fname, d, g)
[x, fs] = audioread(fname);     % read the audio file

y = 0.5*x;
w = y;
k = floor(d*fs/10^3);
for i = 1:numel(d)
    % Create the next w:
    wlen = size(w,1);
    clearvars wnew;
    wnew(:,1) = allpass(w(:,1),k(i), g(i));
    wnew(:,2) = allpass(w(:,2),k(i), g(i));
    
    % Add to y:
    ynew = wnew;
    ynew(1:wlen,:) = ynew(1:wlen,:) + y;
    
    y = ynew; w = wnew;     % update the new variables.
end

sound(y, fs);

end

function y = allpass(x, k, g)

% Determine required forward padding
if abs(g) >= 1
    fwdxpd = (k-1) + 10*k;
else
    fwdxpd = (k-1) + ceil(-2/log10(abs(g)))*k;     % signal decays below 1%
end
zerosfwd = zeros(fwdxpd,1);

% Backward padding should be the same length as k
zerosbkwd = zeros(k,1); 

xext = [zerosbkwd ; x(:); zerosfwd];
extlen = length(xext);

% Produce output y
yext = zeros(extlen,1);
for n = k+(1:(extlen-k))
    yext(n) = g*xext(n) + xext(n-k) - g*yext(n-k);
end

y = yext(k:end);

end


