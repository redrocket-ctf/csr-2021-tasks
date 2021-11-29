SECRET_APP_SITE_METHOD = local
SECRET_APP_SITE = $(SECRET_APP_PKGDIR)/../../../secret_app
SECRET_APP_VERSION = 1.0

define SECRET_APP_BUILD_CMDS
	$(TARGET_MAKE_ENV) $(MAKE) CROSS=$(TARGET_CROSS) CC=$(TARGET_CC) -C $(@D) all
endef

define SECRET_APP_INSTALL_TARGET_CMDS
	$(INSTALL) -D -m 0755 $(@D)/secret_app $(TARGET_DIR)/usr/bin
endef

$(eval $(generic-package))