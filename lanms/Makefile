#CXXFLAGS = -I include  -std=c++11 -O3 $(shell python3-config --cflags)
CXXFLAGS = -I include  -std=c++11 -O3 -I /home/xhyang/anaconda3/envs/tf/include/python3.6m

LDFLAGS = $(shell python3-config --ldflags)

DEPS = lanms.h $(shell find include -xtype f)
CXX_SOURCES = adaptor.cpp include/clipper/clipper.cpp

LIB_SO = adaptor.so

$(LIB_SO): $(CXX_SOURCES) $(DEPS)
	$(CXX) -o $@ $(CXXFLAGS) $(LDFLAGS) $(CXX_SOURCES) --shared -fPIC

clean:
	rm -rf $(LIB_SO)
