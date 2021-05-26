#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-openexr-soname25
Version  : 2.5.5
Release  : 21
URL      : https://github.com/AcademySoftwareFoundation/openexr/archive/v2.5.5/openexr-2.5.5.tar.gz
Source0  : https://github.com/AcademySoftwareFoundation/openexr/archive/v2.5.5/openexr-2.5.5.tar.gz
Summary  : Python bindings for the IlmBase libraries
Group    : Development/Tools
License  : BSD-3-Clause
Requires: compat-openexr-soname25-lib = %{version}-%{release}
Requires: compat-openexr-soname25-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : extra-cmake-modules
BuildRequires : fltk-dev
BuildRequires : freeglut-dev
BuildRequires : glibc-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : zlib-dev

%description
The IlmImfUtil Library
----------------------
The IlmImfUtil library implements an in-memory image data structure, as
well as simple function calls for saving images in OpenEXR files, and for
constructing images from the contents of existing OpenEXR files.

%package lib
Summary: lib components for the compat-openexr-soname25 package.
Group: Libraries
Requires: compat-openexr-soname25-license = %{version}-%{release}

%description lib
lib components for the compat-openexr-soname25 package.


%package license
Summary: license components for the compat-openexr-soname25 package.
Group: Default

%description license
license components for the compat-openexr-soname25 package.


%prep
%setup -q -n openexr-2.5.5
cd %{_builddir}/openexr-2.5.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622068293
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -fzero-call-used-regs=used "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1622068293
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-openexr-soname25
cp %{_builddir}/openexr-2.5.5/LICENSE.md %{buildroot}/usr/share/package-licenses/compat-openexr-soname25/ce40fed41edcb2473538bb84f85ff79e585760b5
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/bin/exr2aces
rm -f %{buildroot}/usr/bin/exrenvmap
rm -f %{buildroot}/usr/bin/exrheader
rm -f %{buildroot}/usr/bin/exrmakepreview
rm -f %{buildroot}/usr/bin/exrmaketiled
rm -f %{buildroot}/usr/bin/exrmultipart
rm -f %{buildroot}/usr/bin/exrmultiview
rm -f %{buildroot}/usr/bin/exrstdattr
rm -f %{buildroot}/usr/include/OpenEXR/Iex.h
rm -f %{buildroot}/usr/include/OpenEXR/IexBaseExc.h
rm -f %{buildroot}/usr/include/OpenEXR/IexErrnoExc.h
rm -f %{buildroot}/usr/include/OpenEXR/IexExport.h
rm -f %{buildroot}/usr/include/OpenEXR/IexForward.h
rm -f %{buildroot}/usr/include/OpenEXR/IexMacros.h
rm -f %{buildroot}/usr/include/OpenEXR/IexMathExc.h
rm -f %{buildroot}/usr/include/OpenEXR/IexMathFloatExc.h
rm -f %{buildroot}/usr/include/OpenEXR/IexMathFpu.h
rm -f %{buildroot}/usr/include/OpenEXR/IexMathIeeeExc.h
rm -f %{buildroot}/usr/include/OpenEXR/IexNamespace.h
rm -f %{buildroot}/usr/include/OpenEXR/IexThrowErrnoExc.h
rm -f %{buildroot}/usr/include/OpenEXR/IlmBaseConfig.h
rm -f %{buildroot}/usr/include/OpenEXR/IlmThread.h
rm -f %{buildroot}/usr/include/OpenEXR/IlmThreadExport.h
rm -f %{buildroot}/usr/include/OpenEXR/IlmThreadForward.h
rm -f %{buildroot}/usr/include/OpenEXR/IlmThreadMutex.h
rm -f %{buildroot}/usr/include/OpenEXR/IlmThreadNamespace.h
rm -f %{buildroot}/usr/include/OpenEXR/IlmThreadPool.h
rm -f %{buildroot}/usr/include/OpenEXR/IlmThreadSemaphore.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathBox.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathBoxAlgo.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathColor.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathColorAlgo.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathEuler.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathExc.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathExport.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathForward.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathFrame.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathFrustum.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathFrustumTest.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathFun.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathGL.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathGLU.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathHalfLimits.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathInt64.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathInterval.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathLimits.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathLine.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathLineAlgo.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathMath.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathMatrix.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathMatrixAlgo.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathNamespace.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathPlane.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathPlatform.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathQuat.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathRandom.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathRoots.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathShear.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathSphere.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathVec.h
rm -f %{buildroot}/usr/include/OpenEXR/ImathVecAlgo.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfAcesFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfArray.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfB44Compressor.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfBoxAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfCRgbaFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfChannelList.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfChannelListAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfChromaticities.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfChromaticitiesAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfCompositeDeepScanLine.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfCompression.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfCompressionAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfConvert.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepCompositing.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepFrameBuffer.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepImage.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepImageChannel.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepImageIO.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepImageLevel.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepImageState.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepImageStateAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepScanLineInputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepScanLineInputPart.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepScanLineOutputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepScanLineOutputPart.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepTiledInputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepTiledInputPart.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepTiledOutputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDeepTiledOutputPart.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfDoubleAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfEnvmap.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfEnvmapAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfExport.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfFlatImage.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfFlatImageChannel.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfFlatImageIO.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfFlatImageLevel.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfFloatAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfFloatVectorAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfForward.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfFrameBuffer.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfFramesPerSecond.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfGenericInputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfGenericOutputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfHeader.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfHuf.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfIO.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfImage.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfImageChannel.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfImageChannelRenaming.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfImageDataWindow.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfImageIO.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfImageLevel.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfInputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfInputPart.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfInt64.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfIntAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfKeyCode.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfKeyCodeAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfLineOrder.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfLineOrderAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfLut.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfMatrixAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfMultiPartInputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfMultiPartOutputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfMultiView.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfName.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfNamespace.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfOpaqueAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfOutputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfOutputPart.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfPartHelper.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfPartType.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfPixelType.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfPreviewImage.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfPreviewImageAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfRational.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfRationalAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfRgba.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfRgbaFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfRgbaYca.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfSampleCountChannel.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfStandardAttributes.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfStdIO.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfStringAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfStringVectorAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTestFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfThreading.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTileDescription.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTileDescriptionAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTiledInputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTiledInputPart.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTiledOutputFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTiledOutputPart.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTiledRgbaFile.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTimeCode.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfTimeCodeAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfUtilExport.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfVecAttribute.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfVersion.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfWav.h
rm -f %{buildroot}/usr/include/OpenEXR/ImfXdr.h
rm -f %{buildroot}/usr/include/OpenEXR/OpenEXRConfig.h
rm -f %{buildroot}/usr/include/OpenEXR/PyIex.h
rm -f %{buildroot}/usr/include/OpenEXR/PyIexExport.h
rm -f %{buildroot}/usr/include/OpenEXR/PyIexTypeTranslator.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImath.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathAutovectorize.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathBasicTypes.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathBox.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathBoxArrayImpl.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathColor.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathColor3ArrayImpl.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathColor4Array2DImpl.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathColor4ArrayImpl.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathDecorators.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathEuler.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathExport.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathFixedArray.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathFixedArray2D.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathFixedMatrix.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathFixedVArray.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathFrustum.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathFun.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathLine.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathM44Array.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathMathExc.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathMatrix.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathOperators.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathPlane.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathQuat.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathRandom.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathShear.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathStringArray.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathStringArrayRegister.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathStringTable.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathTask.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathUtil.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathVec.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathVec2Impl.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathVec3ArrayImpl.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathVec3Impl.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathVec4ArrayImpl.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathVec4Impl.h
rm -f %{buildroot}/usr/include/OpenEXR/PyImathVecOperators.h
rm -f %{buildroot}/usr/include/OpenEXR/half.h
rm -f %{buildroot}/usr/include/OpenEXR/halfExport.h
rm -f %{buildroot}/usr/include/OpenEXR/halfFunction.h
rm -f %{buildroot}/usr/include/OpenEXR/halfLimits.h
rm -f %{buildroot}/usr/lib/python3.9/site-packages/iex.so
rm -f %{buildroot}/usr/lib/python3.9/site-packages/imath.so
rm -f %{buildroot}/usr/lib64/cmake/IlmBase/IlmBaseConfig.cmake
rm -f %{buildroot}/usr/lib64/cmake/IlmBase/IlmBaseConfigVersion.cmake
rm -f %{buildroot}/usr/lib64/cmake/IlmBase/IlmBaseTargets-relwithdebinfo.cmake
rm -f %{buildroot}/usr/lib64/cmake/IlmBase/IlmBaseTargets.cmake
rm -f %{buildroot}/usr/lib64/cmake/OpenEXR/OpenEXRConfig.cmake
rm -f %{buildroot}/usr/lib64/cmake/OpenEXR/OpenEXRConfigVersion.cmake
rm -f %{buildroot}/usr/lib64/cmake/OpenEXR/OpenEXRTargets-relwithdebinfo.cmake
rm -f %{buildroot}/usr/lib64/cmake/OpenEXR/OpenEXRTargets.cmake
rm -f %{buildroot}/usr/lib64/cmake/PyIlmBase/PyIlmBaseConfig-relwithdebinfo.cmake
rm -f %{buildroot}/usr/lib64/cmake/PyIlmBase/PyIlmBaseConfig.cmake
rm -f %{buildroot}/usr/lib64/cmake/PyIlmBase/PyIlmBaseConfigVersion.cmake
rm -f %{buildroot}/usr/lib64/libHalf-2_5.so
rm -f %{buildroot}/usr/lib64/libHalf.so
rm -f %{buildroot}/usr/lib64/libIex-2_5.so
rm -f %{buildroot}/usr/lib64/libIex.so
rm -f %{buildroot}/usr/lib64/libIexMath-2_5.so
rm -f %{buildroot}/usr/lib64/libIexMath.so
rm -f %{buildroot}/usr/lib64/libIlmImf-2_5.so
rm -f %{buildroot}/usr/lib64/libIlmImf.so
rm -f %{buildroot}/usr/lib64/libIlmImfUtil-2_5.so
rm -f %{buildroot}/usr/lib64/libIlmImfUtil.so
rm -f %{buildroot}/usr/lib64/libIlmThread-2_5.so
rm -f %{buildroot}/usr/lib64/libIlmThread.so
rm -f %{buildroot}/usr/lib64/libImath-2_5.so
rm -f %{buildroot}/usr/lib64/libImath.so
rm -f %{buildroot}/usr/lib64/libPyIex_Python3_9-2_5.so
rm -f %{buildroot}/usr/lib64/libPyImath_Python3_9-2_5.so
rm -f %{buildroot}/usr/lib64/pkgconfig/IlmBase.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/OpenEXR.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/PyIlmBase.pc
rm -f %{buildroot}/usr/share/doc/OpenEXR/InterpretingDeepPixels.pdf
rm -f %{buildroot}/usr/share/doc/OpenEXR/MultiViewOpenEXR.pdf
rm -f %{buildroot}/usr/share/doc/OpenEXR/OpenEXRFileLayout.pdf
rm -f %{buildroot}/usr/share/doc/OpenEXR/ReadingAndWritingImageFiles.pdf
rm -f %{buildroot}/usr/share/doc/OpenEXR/TechnicalIntroduction.pdf
rm -f %{buildroot}/usr/share/doc/OpenEXR/TheoryDeepPixels.pdf
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/drawImage.cpp
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/drawImage.h
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/generalInterfaceExamples.cpp
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/generalInterfaceExamples.h
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/generalInterfaceTiledExamples.cpp
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/generalInterfaceTiledExamples.h
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/lowLevelIoExamples.cpp
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/lowLevelIoExamples.h
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/main.cpp
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/namespaceAlias.h
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/previewImageExamples.cpp
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/previewImageExamples.h
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/rgbaInterfaceExamples.cpp
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/rgbaInterfaceExamples.h
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/rgbaInterfaceTiledExamples.cpp
rm -f %{buildroot}/usr/share/doc/OpenEXR/examples/rgbaInterfaceTiledExamples.h

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libHalf-2_5.so.25
/usr/lib64/libHalf-2_5.so.25.0.4
/usr/lib64/libIex-2_5.so.25
/usr/lib64/libIex-2_5.so.25.0.4
/usr/lib64/libIexMath-2_5.so.25
/usr/lib64/libIexMath-2_5.so.25.0.4
/usr/lib64/libIlmImf-2_5.so.25
/usr/lib64/libIlmImf-2_5.so.25.0.4
/usr/lib64/libIlmImfUtil-2_5.so.25
/usr/lib64/libIlmImfUtil-2_5.so.25.0.4
/usr/lib64/libIlmThread-2_5.so.25
/usr/lib64/libIlmThread-2_5.so.25.0.4
/usr/lib64/libImath-2_5.so.25
/usr/lib64/libImath-2_5.so.25.0.4
/usr/lib64/libPyIex_Python3_9-2_5.so.25
/usr/lib64/libPyIex_Python3_9-2_5.so.25.0.4
/usr/lib64/libPyImath_Python3_9-2_5.so.25
/usr/lib64/libPyImath_Python3_9-2_5.so.25.0.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-openexr-soname25/ce40fed41edcb2473538bb84f85ff79e585760b5
