{ pkgs }: {
    deps = [
      pkgs.geckodriver
      # pkgs.ungoogled-chromium
      # pkgs.chromedriver
      pkgs.chromium
      pkgs.chromedriver
      pkgs.cowsay
    ];
}