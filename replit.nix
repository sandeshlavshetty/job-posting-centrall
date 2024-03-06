{ pkgs }: {
    deps = [
      pkgs.nss_latest.tools
      pkgs.geckodriver
      # pkgs.ungoogled-chromium
      # pkgs.chromedriver
      pkgs.chromium
      pkgs.chromedriver
      pkgs.cowsay
    ];
}